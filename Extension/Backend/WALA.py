from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import threading
import textComp as tx
import imageText as it
import vicramCalc as vc
import whiteSpace as ws
import EntropyCalc as im
import crawler as cw
import reportGen as report
import requests
from selenium import webdriver
from threading import Semaphore
import time


# Function to get screen size using Selenium
def get_screen_size():
    try:
        # Initialize a Selenium webdriver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Open the browser window maximized
        driver = webdriver.Chrome(
            options=options)  # You may need to adjust this based on your browser and webdriver setup

        # Open a webpage
        driver.get('https://www.example.com')  # Open any webpage

        # Get window size
        window_size = driver.get_window_size()

        # Extract width and height
        width = window_size['width']
        height = window_size['height']

        # Close the webdriver
        driver.quit()

        return width, height
    except Exception as e:
        print("Error getting screen size:", e)
        return None


app = Flask(__name__)

cors = CORS(app)

# Initialize semaphore with a maximum number of concurrent requests
semaphore = Semaphore(5)  # Adjust the value as needed


@app.route("/scan", methods=['GET'])
def Scan():
    start_time = time.time()
    global screen_size
    screen_size = get_screen_size()
    print("Screen size =", screen_size)
    result = {
        "Visual Complexity": 0,
        "Distinguishability": 0,
        "Text Image Ratio": 0,
        "Text Complexity": 0,
        "Image Complexity": 0,
        "Autism Friendliness Status": "?",
    }
    url = request.args.get('data1')
    visualcomp = request.args.get('data2')
    distin = request.args.get('data3')
    text_image = request.args.get('data4')
    textc = request.args.get('data5')
    image = request.args.get('data6')
    radioval = request.args.get('data7')

    print(
        "Main URL: " + url + "\nVisual Complexity Selected? " + visualcomp + " Distinguishability Selected? " + distin + " Text_Image Ratio Selected? " + text_image + " Text Complexity Selected? " + textc + "\nImage Complexity Selected? " + image + " Crawling Method? " + radioval)

    if radioval == 'w':
        inner_urls = cw.crawler(url)
        inner_urls.insert(0, url)
    else:
        inner_urls = [url]

    def calculate_all_complexities_with_throttling(inner_url, index, vis, dist, te_im, tex, ima):
        try:
            semaphore.acquire()  # Acquire semaphore before making a request
            response = requests.get(inner_url, timeout=240, headers={"User-Agent":"XY"})
            if response.status_code != 200:
                response = requests.get(inner_url, timeout=240, headers={"User-Agent":"XY"} ,verify=False)
            if response.status_code == 200:
                # Process response...
                threads1 = []
                if visualcomp == "true":
                    threads1.append(threading.Thread(target=calculate_visual_complexity, args=(inner_url, vis, index)))
                if distin == "true":
                    threads1.append(
                        threading.Thread(target=calculate_distinguishability, args=(inner_url, dist, index)))
                if text_image == "true":
                    threads1.append(threading.Thread(target=calculate_text_image_ratio, args=(response, te_im, index)))
                    print("Thread__1 {} sended".format(index))
                if textc == "true":
                    threads1.append(threading.Thread(target=calculate_text_complexity, args=(response, tex, index)))
                    print("Thread__1 {} sended".format(index))
                if image == "true":
                    threads1.append(threading.Thread(target=calculate_image_complexity,
                                                     args=(inner_url, response, ima, index, screen_size)))

                for thread in threads1:
                    thread.start()

                # Wait Threads
                for thread in threads1:
                    thread.join()
        except Exception as e:
            print(f"Error processing URL {inner_url}: {e}")
        finally:
            semaphore.release()  # Release semaphore after processing

    def calculate_visual_complexity(url, vis, index):
        out = vc.vicramcalc1("example_role", url)
        vis[index - 1] = out
        if index == 1:
            result["Visual Complexity"] = out

    def calculate_distinguishability(url, dist, index):
        out = ws.vicramcalc("example_role", url)
        dist[index - 1] = out
        if index == 1:
            result["Distinguishability"] = out

    def calculate_text_image_ratio(response, te_im, index):
        out = it.calculate_image_text_ratio(response)
        te_im[index - 1] = out
        if index == 1:
            result["Text Image Ratio"] = out

    def calculate_text_complexity(response, tex, index):
        out = tx.text_complexity(response)
        tex[index - 1] = out
        if index == 1:
            result["Text Complexity"] = out

    def calculate_image_complexity(url, response, ima, index, screen_size):
        out = im.calculate_image_complexity(response, url, screen_size)
        ima[index - 1] = out
        if index == 1:
            result["Image Complexity"] = out

    def generate_report():
        normalized_dist = []
        normalized_vis = []
        normalized_tex = []
        normalized_ima = []
        normalized_te_im = []
        global pdf
        pdf = report.getsinglereport(dist[0], vis[0], tex[0], ima[0], te_im[0], url)
        total = []
        total_score_ex = []

        total_dis = sum(dist) / len(inner_urls)
        total_vis = sum(vis) / len(inner_urls)
        total_ima = sum(ima) / len(inner_urls)
        total_tex = sum(tex) / len(inner_urls)
        total_te_im = sum(te_im) / len(inner_urls)
        pdf = report.total_scorepdf(total_dis, total_vis, total_tex, total_ima, total_te_im, pdf)

        for i, x in enumerate(inner_urls):
            # Normalize metric values for current URL and append to lists
            normalized_dist.append(normalize(dist[i], 1) if dist[i] != -1 else 0)
            normalized_vis.append(normalize(vis[i], 2) if vis[i] != -1 else 0)
            normalized_tex.append(normalize(tex[i], 3) if tex[i] != -1 else 0)
            normalized_ima.append(normalize(ima[i], 4) if ima[i] != -1 else 0)
            normalized_te_im.append(normalize(te_im[i], 5) if te_im[i] != -1 else 0)

        for i, x in enumerate(inner_urls):
            # Compute total score for current URL
            # Count only the metrics that were normalized
            num_metrics = sum(
                1 for val in
                [normalized_dist[i], normalized_vis[i], normalized_tex[i], normalized_ima[i], normalized_te_im[i]] if
                val != 0)
            # Assuming normalized_dist, normalized_vis, normalized_tex, normalized_ima, normalized_te_im are defined
            metrics = [normalized_dist[i], normalized_vis[i], normalized_tex[i], normalized_ima[i], normalized_te_im[i]]

            # Filter out zero values
            non_zero_metrics = [metric for metric in metrics if metric != 0]

            # Calculate total_score based on non-zero metrics
            if non_zero_metrics:  # Check if the list is not empty
                total_score = sum(non_zero_metrics) / len(non_zero_metrics)
            else:
                total_score = 0  # If all metrics are zero, set total_score to 0

            total_score_ex.append(total_score)
            total_score = f"{total_score:.2f}"

            total_score_str = str(total_score) + "/5"
            total.append(total_score_str)

            # Add metrics for current URL
            pdf = report.metricadd_pdf(dist[i], vis[i], tex[i], ima[i], te_im[i], x, pdf)

        avg_total_score = 0
        for num in total_score_ex:
            avg_total_score = avg_total_score + num

        avg_total_score = avg_total_score/len(inner_urls)

        avg_total_score = int(avg_total_score)

        if avg_total_score == 0:
            result["Autism Friendliness Status"] = "Very Bad"
        if avg_total_score == 1:
            result["Autism Friendliness Status"] = "Bad"
        if avg_total_score == 2:
            result["Autism Friendliness Status"] = "Okay"
        if avg_total_score == 3:
            result["Autism Friendliness Status"] = "Good"
        if avg_total_score == 4:
            result["Autism Friendliness Status"] = "Very Good"

        pdf = report.addtable(inner_urls, dist, vis, tex, ima, te_im, total, pdf)
        return pdf

    def normalize(value, metric):
        if metric == 1:
            return (value / 1) * 4 + 1  # Normalize to the range [1, 5]
        if metric == 2:
            return (value / 10) * 4 + 1
        if metric == 3:
            return (value / 500) * 4 + 1
        if metric == 4:
            return (value / 1) * 4 + 1
        if metric == 5:
            return (value / 250) * 4 + 1

    index = 0
    if visualcomp == "true":
        vis = [0] * len(inner_urls)
    else:
        vis = [-1] * len(inner_urls)
    if distin == "true":
        dist = [0] * len(inner_urls)
    else:
        dist = [-1] * len(inner_urls)
    if text_image == "true":
        te_im = [0] * len(inner_urls)
    else:
        te_im = [-1] * len(inner_urls)
    if textc == "true":
        tex = [0] * len(inner_urls)
    else:
        tex = [-1] * len(inner_urls)
    if image == "true":
        # screen_size = get_screen_size()
        ima = [0] * len(inner_urls)
    else:
        ima = [-1] * len(inner_urls)
    threads = []

    for inner_url in inner_urls:
        index = index + 1
        threads.append(
            threading.Thread(target=calculate_all_complexities_with_throttling,
                             args=(inner_url, index, vis, dist, te_im, tex, ima)))
        print("Thread {} sended".format(index))

    if visualcomp == "false":
        result["Visual Complexity"] = 0
    if distin == "false":
        result["Distinguishability"] = 0
    if text_image == "false":
        result["Text Image Ratio"] = 0
    if textc == "false":
        result["Text Complexity"] = 0
    if image == "false":
        result["Image Complexity"] = 0

    # Start Threads
    for thread in threads:
        thread.start()

    # Wait Threads
    for thread in threads:
        thread.join()

    pdf = generate_report()
    pdf.output('WALA_Report.pdf')
    print(inner_urls, tex)

    print("--- %s seconds ---" % (time.time() - start_time))
    # return jsonify({'message': f'Data received: {result}'})
    print(result)
    return jsonify(result)


@app.route('/generate_report', methods=['GET', 'POST'])
def downloadReport():
    return send_file('WALA_Report.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
