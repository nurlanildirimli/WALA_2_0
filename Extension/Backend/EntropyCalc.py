from bs4 import BeautifulSoup
from urllib.parse import urljoin
import subprocess
import imageMain as im
import relativeImageSize as t


def get_image_dimensions(webpage_url, image_url):
    try:
        # Define the command to run the JavaScript file with Node.js
        command = ['node', 'relativeImageSize.js', webpage_url, image_url]

        # Execute the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the process to finish and capture the output
        stdout, stderr = process.communicate()

        # Decode the output
        stdout_str = stdout.decode('utf-8')
        stderr_str = stderr.decode('utf-8')

        # Process the output to extract image dimensions
        # Here we assume the output is in the format "width,height"
        if stdout_str.strip():
            width, height = map(int, stdout_str.strip().split(','))
            return width, height
        else:
            print(f"No dimensions found for image: {image_url}")
            return None, None
    except Exception as e:
        print(f"Error getting image dimensions for {image_url}: {e}")
        return None, None


def parse_output(output):
    try:
        # Split the output string by comma and convert the parts to integers
        width, height = map(int, output.strip().split(','))
        return width, height
    except ValueError as e:
        print(f"Error parsing output: {e}")
        return None, None


def calculate_image_complexity(response, url, screen_size):
    try:
        image_complexity = 0
        total_image_weight = 0

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all('img')
        num_images = len(img_tags)
        image_data = t.get_effective_image_sizes(url, screen_size)
        image_urls = [data['url'] for data in image_data]

        print("Total Number of images found: ", num_images)  # Print number of images found
        print("Number of images discarded: ", num_images - len(image_data))
        print("Valid Number of Images: ", len(image_data))
        sizes = [f"{data['width']}x{data['height']}" for data in image_data]

        for index, data in enumerate(image_data):
            # Extract image URL from the img tag
            img_url = image_urls[index]

            # Print image URL for debugging
            print("Image URL:", img_url)

            entropy_value = im.calculate_normalized_entropy_from_url(urljoin(url, img_url))

            if entropy_value != -1:
                normalized_img_size = int(sizes[index].split('x')[0]) * int(sizes[index].split('x')[1]) / (screen_size[0] * screen_size[1])

                weight = normalized_img_size

                print("Weight:", weight)  # Print weight for debugging

                # Accumulate total weight
                total_image_weight += weight
                # Update image complexity
                image_complexity += entropy_value * weight

        # Calculate average image complexity
        if total_image_weight > 0:
            return image_complexity / total_image_weight
        else:
            return 0  # To avoid division by zero if there are no images

    except Exception as e:
        print(f"Error processing webpage: {e}")
        return None
