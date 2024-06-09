from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image(r'C:\Users\dani-\OneDrive\Desktop\WALA 2.0\WALALogo.png', 15, 5, 30)
        self.set_font('times', 'BU', 30)
        self.cell(50)
        self.cell(90, 15, 'WALA Report', border=1, align='C', ln=1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('times', '', 14)
        total_pages = self.page_no()
        self.cell(0, 10, f'Page {self.page_no()}/{total_pages}', align='C')


def getsinglereport(d, v, t, i, r, url):
    pdf = PDF('P', 'mm')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font('times', 'B', 16)
    pdf.cell(0, 8, 'Metrics and their definitions:', ln=1)
    pdf.ln(5)
    pdf.set_font('times', 'B', 14)
    pdf.cell(0, 8, '1) Distinguishability:', ln=1)
    pdf.set_font('times', '', 14)
    pdf.cell(0, 8, 'Refers to the clarity and ease with which various elements on a webpage can be perceived and ',
             ln=1)
    pdf.cell(0, 8, 'understood, including the white space ratio between components. White space, or the empty space',
             ln=1)
    pdf.cell(0, 8, 'between elements, plays a crucial role in enhancing readability and visual clarity.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.cell(0, 8, '2) Visual Complexity:', ln=1)
    pdf.set_font('times', '', 14)
    pdf.cell(0, 8, 'Refers to how crowded or busy a webpage appears, including the number of images, text, buttons,',
             ln=1)
    pdf.cell(0, 8, 'and other elements present on the page. ', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.cell(0, 8, '3) Text Complexity:', ln=1)
    pdf.set_font('times', '', 14)
    pdf.cell(0, 8, 'Refers to the challenge presented by the language used and the organization of written content ',
             ln=1)
    pdf.cell(0, 8, 'on a webpage. This includes factors such as sentence length, vocabulary choice, and the presence ',
             ln=1)
    pdf.cell(0, 8, 'of complex syntax.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.cell(0, 8, '4) Image Complexity:', ln=1)
    pdf.set_font('times', '', 14)
    pdf.cell(0, 8, 'Refers to the intricacy and density of visual elements, including pictures, graphics, icons,', ln=1)
    pdf.cell(0, 8, 'and texture, on a webpage.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.cell(0, 8, '5) Text-Image Ratio:', ln=1)
    pdf.set_font('times', '', 14)
    pdf.cell(0, 8, 'Refers to the ratio of the amount of text on a page to the number of images.', ln=1)
    pdf.cell(0, 8, '____________________________________________________________________________', ln=1)
    return pdf


def metricadd_pdf(d, v, t, i, r, url, pdf):
    f_d = "{:.2f}".format(d)
    f_v = "{:.2f}".format(v)
    f_t = "{:.2f}".format(t)
    f_i = "{:.2f}".format(i)
    f_r = "{:.2f}".format(r)
    pdf.ln(5)
    pdf.set_font('times', 'B', 14)
    pdf.cell(15, 8, 'URL : ')
    pdf.set_font('times', '', 14)
    pdf.cell(0, 8, url, ln=1)
    pdf.ln(5)
    pdf.set_font('times', 'B', 14)
    if d != -1:
        pdf.cell(0, 8, f'Distinguishibility score : {f_d}', ln=1)
    else:
        pdf.cell(0, 8, f'Distinguishibility score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if d >= 0 and d < 0.2:
        pdf.cell(0, 8,
                 'The score is classified as very bad, thus making it extremely difficult for people on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Increase white space between elements to reduce clutter and improve visibility.', ln=1)
    elif d >= 0.2 and d < 0.4:
        pdf.cell(0, 8, 'The score is classified as bad, thus making it challenging for people on the spectrum', ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' :Ensure padding and margins around text and interactive elements for clearer distinction.',
                 ln=1)
    elif d >= 0.4 and d < 0.6:
        pdf.cell(0, 8, 'The score is classified as ok, thus making it somewhat challenging for people on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components .', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8,
                 ' :Balance white space distribution to maintain a harmonious layout without overwhelming the user.',
                 ln=1)
    elif d >= 0.6 and d < 0.8:
        pdf.cell(0, 8, 'The score is classified as good, thus making it easy for people on the spectrum', ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components .', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' :Optimize white space to guide users focus and enhance readability without sacrificing', ln=1)
        pdf.cell(0, 8, 'content density.', ln=1)
    elif d >= 0.8:
        pdf.cell(0, 8, 'The score is classified as very good, thus making it very simple for people on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components .', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' :Use white space strategically to create a clean and intuitive interface that facilitates ',
                 ln=1)
        pdf.cell(0, 8, 'effortless navigation.', ln=1)
    elif d == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.ln(10)
    if v != -1:
        pdf.cell(0, 8, f'Visual Complexity score : {f_v}', ln=1)
    else:
        pdf.cell(0, 8, f'Visual Complexity score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if v <= 10 and v > 8:
        pdf.cell(0, 8, 'The score is classified as very bad, making it extremely challenging for individuals', ln=1)
        pdf.cell(0, 8,
                 'on the spectrum to differentiate between various components due to excessive visual clutter and.',
                 ln=1)
        pdf.cell(0, 8, ' complexity', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Simplify the layout by reducing the number of visual elements and removing ', ln=1)
        pdf.cell(0, 8, 'unnecessary decorative elements.', ln=1)
    elif v <= 8 and v > 6:
        pdf.cell(0, 8, 'The score is classified as bad, making it difficult for individuals on the spectrum to ', ln=1)
        pdf.cell(0, 8, 'differentiate between varying components due to high visual complexity and clutter.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Streamline the design by prioritizing essential content and removing non-essential ', ln=1)
        pdf.cell(0, 8, 'elements.', ln=1)
    elif v <= 6 and v > 4:
        pdf.cell(0, 8,
                 'The score is classified as okay, making it somewhat challenging for individuals on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between components due to moderate visual complexity.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Implement clear navigation paths to help users navigate through the webpage easily.', ln=1)
    elif v <= 4 and v > 2:
        pdf.cell(0, 8, 'The score is classified as good, indicating a manageable level of visual complexity', ln=1)
        pdf.cell(0, 8, 'for individuals on the spectrum to differentiate between components with relative ease.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Maintain a balance between visual interest and simplicity to create an engaging yet ', ln=1)
        pdf.cell(0, 8, 'accessible design.', ln=1)
    elif v <= 2 and v >= 0:
        pdf.cell(0, 8, 'The score is classified as very good, indicating minimal visual complexity, making it', ln=1)
        pdf.cell(0, 8, 'easy for individuals on the spectrum to differentiate between components effortlessly.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Strive for a visually pleasing design that remains simple and easy to comprehend.', ln=1)
    elif v == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.ln(10)
    pdf.set_font('times', 'B', 14)
    if t != -1:
        pdf.cell(0, 8, f'Text Complexity score : {f_t}', ln=1)
    else:
        pdf.cell(0, 8, f'Text Complexity score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if t <= 10 and t >= 0:
        pdf.cell(0, 8, 'The score is classified as very good, indicating minimal text complexity, making it', ln=1)
        pdf.cell(0, 8, 'highly accessible and understandable for individuals on the spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Define any special or techincal terms to improve understanding.', ln=1)
    elif t > 10 and t <= 14:
        pdf.cell(0, 8, 'The score is classified as good, indicating a low level of text complexity,', ln=1)
        pdf.cell(0, 8, 'which is generally easy for individuals on the spectrum to comprehend.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Divide complex sentences into seperate sentences.', ln=1)
    elif t > 14 and t < 20:
        pdf.cell(0, 8, 'The score is classified as okay, suggesting a moderate level of text complexity,', ln=1)
        pdf.cell(0, 8, 'which may present some challenges for individuals on the spectrum but remains manageable ',
                 ln=1)
        pdf.cell(0, 8, 'with effort.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Define technical terms and provide necessary informations.', ln=1)
    elif t >= 20 and t <= 30:
        pdf.cell(0, 8, 'The score is classified as bad, indicating a high level of text complexity, which can pose',
                 ln=1)
        pdf.cell(0, 8,
                 'significant difficulties for individuals on the spectrum in understanding and processing the content.',
                 ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Simplify language and sentence structure to make the text more accessible and easier ', ln=1)
        pdf.cell(0, 8, 'to comprehend.', ln=1)
    elif t > 30:
        pdf.cell(0, 8, 'The score is classified as very bad, representing an extremely high level of text complexity,',
                 ln=1)
        pdf.cell(0, 8,
                 'making it nearly impossible for individuals on the spectrum to comprehend the content effectively.',
                 ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Rewrite the text using clear, concise language and shorter sentences to drastically ', ln=1)
        pdf.cell(0, 8, 'reduce complexity.', ln=1)
    elif t == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.ln(10)
    if i != -1:
        pdf.cell(0, 8, f'Image Complexity score : {f_i}', ln=1)
    else:
        pdf.cell(0, 8, f'Image Complexity score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if i <= 0.2 and i >= 0:
        pdf.cell(0, 8, 'The score is classified as very good, indicating minimal visual clutter with clear ', ln=1)
        pdf.cell(0, 8,
                 'outlines and simple shapes, making it highly accessible and comfortable for individuals on the ',
                 ln=1)
        pdf.cell(0, 8, 'spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Ensure that images are appropriately sized to prevent overwhelming the viewer.', ln=1)
    elif i <= 0.4 and i > 0.2:
        pdf.cell(0, 8, 'The score is classified as good, suggesting the use of images with moderate complexity ', ln=1)
        pdf.cell(0, 8,
                 'and a harmonious color palette, providing a visually pleasing experience for individuals on the',
                 ln=1)
        pdf.cell(0, 8, 'spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Choose textures that are gentle and non-distracting.', ln=1)
    elif i <= 0.6 and i > 0.4:
        pdf.cell(0, 8, 'The score is classified as okay, indicating controlled visual elements and a restrained ', ln=1)
        pdf.cell(0, 8, 'color scheme, which may present some challenges for individuals on the spectrum but remains ',
                 ln=1)
        pdf.cell(0, 8, 'manageable with effort.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Opt for textures that are subtle and uniform across the image.', ln=1)
    elif i <= 0.8 and i > 0.6:
        pdf.cell(0, 8, 'The score is classified as bad, suggesting images with excessive details or vibrant colors ',
                 ln=1)
        pdf.cell(0, 8, 'that may overwhelm sensory processing, posing significant difficulties for individuals on the ',
                 ln=1)
        pdf.cell(0, 8, 'spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8,
                 ' : Avoid images with excessive details or intricate patterns that may overwhelm sensory processing,',
                 ln=1)
        pdf.cell(0, 8, 'and minimize the use of vibrant colors or high-contrast combinations.', ln=1)
    elif i > 0.8:
        pdf.cell(0, 8, 'The score is classified as very bad, representing images with high visual complexity and ',
                 ln=1)
        pdf.cell(0, 8, 'sensory stimuli, making it nearly impossible for individuals with autism to process ', ln=1)
        pdf.cell(0, 8, 'effectively and causing significant discomfort.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Use a muted color palette with minimal variation to promote calmness, and opt ', ln=1)
        pdf.cell(0, 8, 'for smooth, uniform textures to minimize sensory discomfort.', ln=1)
    elif i == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.ln(10)
    if r != -1:
        pdf.cell(0, 8, f'Text-Image Ratio score : {f_r}', ln=1)
    else:
        pdf.cell(0, 8, f'Text-Image Ratio score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if r <= 50 and r >= 0:
        pdf.cell(0, 8, 'The ratio is classified as very good, indicating a well-balanced mix of text and images,', ln=1)
        pdf.cell(0, 8, 'providing sufficient visual support and engagement for users on the autism spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Maintain the current balance between text and images, as it provides an optimal mix ', ln=1)
        pdf.cell(0, 8, 'of textual information and visual support.', ln=1)
    elif r <= 100 and r > 50:
        pdf.cell(0, 8, 'The ratio is classified as good, suggesting a slightly higher emphasis on textual ', ln=1)
        pdf.cell(0, 8, 'content but still maintaining a reasonable balance with images, contributing to an overall ',
                 ln=1)
        pdf.cell(0, 8, 'engaging user experience.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Consider increasing the number of images or visual elements slightly to provide additional ',
                 ln=1)
        pdf.cell(0, 8, 'visual support and engagement.', ln=1)
    elif r <= 150 and r > 100:
        pdf.cell(0, 8, 'The ratio is classified as okay, indicating a moderate imbalance between text and images, ',
                 ln=1)
        pdf.cell(0, 8, 'which may present some challenges for users in terms of visual support and engagement.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Ensure that images are used strategically to enhance understanding and engagement.', ln=1)
    elif r <= 200 and r > 150:
        pdf.cell(0, 8, 'The ratio is classified as bad, suggesting a significant imbalance with an excessive ', ln=1)
        pdf.cell(0, 8, 'emphasis on textual content over images, potentially leading to decreased visual ', ln=1)
        pdf.cell(0, 8, 'engagement and accessibility for users.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Decrease the amount of textual content and increase the number of images ', ln=1)
        pdf.cell(0, 8, 'to create a more balanced and engaging user experience.', ln=1)
    elif r <= 250 and r > 200:
        pdf.cell(0, 8, 'The ratio is classified as very bad, indicating an extreme imbalance with an ', ln=1)
        pdf.cell(0, 8, 'overwhelming emphasis on textual content, severely limiting visual support ', ln=1)
        pdf.cell(0, 8, 'and engagement for users on the autism spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Significantly reduce the amount of textual content and substantially increase ', ln=1)
        pdf.cell(0, 8, 'the number of images to create a more visually engaging and accessible user experience,', ln=1)
        pdf.cell(0, 8, 'while also ensuring that images are used strategically to convey information and enhance ',
                 ln=1)
        pdf.cell(0, 8, 'comprehension for users on the autism spectrum.', ln=1)
    elif r == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.cell(0, 8, '____________________________________________________________________________', ln=1)
    return pdf


def total_scorepdf(d, v, t, i, r, pdf):
    f_d = "{:.2f}".format(d)
    f_v = "{:.2f}".format(v)
    f_t = "{:.2f}".format(t)
    f_i = "{:.2f}".format(i)
    f_r = "{:.2f}".format(r)
    pdf.set_font('times', 'B', 14)
    pdf.cell(0, 8, 'Overall Score : ', ln=1)
    if d != -1:
        pdf.cell(0, 8, f'Distinguishibility score : {f_d}', ln=1)
    else:
        pdf.cell(0, 8, f'Distinguishibility score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if d >= 0 and d < 0.2:
        pdf.cell(0, 8,
                 'The score is classified as very bad, thus making it extremely difficult for people on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Increase white space between elements to reduce clutter and improve visibility.', ln=1)
    elif d >= 0.2 and d < 0.4:
        pdf.cell(0, 8, 'The score is classified as bad, thus making it challenging for people on the spectrum', ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' :Ensure padding and margins around text and interactive elements for clearer distinction.',
                 ln=1)
    elif d >= 0.4 and d < 0.6:
        pdf.cell(0, 8, 'The score is classified as ok, thus making it somewhat challenging for people on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components .', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8,
                 ' :Balance white space distribution to maintain a harmonious layout without overwhelming the user.',
                 ln=1)
    elif d >= 0.6 and d < 0.8:
        pdf.cell(0, 8, 'The score is classified as good, thus making it easy for people on the spectrum', ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components .', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' :Optimize white space to guide users focus and enhance readability without sacrificing', ln=1)
        pdf.cell(0, 8, 'content density.', ln=1)
    elif d >= 0.8:
        pdf.cell(0, 8, 'The score is classified as very good, thus making it very simple for people on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between varying components .', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' :Use white space strategically to create a clean and intuitive interface that facilitates ',
                 ln=1)
        pdf.cell(0, 8, 'effortless navigation.', ln=1)
    elif d == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.ln(10)
    if v != -1:
        pdf.cell(0, 8, f'Visual Complexity score : {f_v}', ln=1)
    else:
        pdf.cell(0, 8, f'Visual Complexity score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if v <= 10 and v > 8:
        pdf.cell(0, 8, 'The score is classified as very bad, making it extremely challenging for individuals', ln=1)
        pdf.cell(0, 8,
                 'on the spectrum to differentiate between various components due to excessive visual clutter and.',
                 ln=1)
        pdf.cell(0, 8, ' complexity', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Simplify the layout by reducing the number of visual elements and removing ', ln=1)
        pdf.cell(0, 8, 'unnecessary decorative elements.', ln=1)
    elif v <= 8 and v > 6:
        pdf.cell(0, 8, 'The score is classified as bad, making it difficult for individuals on the spectrum to ', ln=1)
        pdf.cell(0, 8, 'differentiate between varying components due to high visual complexity and clutter.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Streamline the design by prioritizing essential content and removing non-essential ', ln=1)
        pdf.cell(0, 8, 'elements.', ln=1)
    elif v <= 6 and v > 4:
        pdf.cell(0, 8,
                 'The score is classified as okay, making it somewhat challenging for individuals on the spectrum',
                 ln=1)
        pdf.cell(0, 8, 'to differentiate between components due to moderate visual complexity.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Implement clear navigation paths to help users navigate through the webpage easily.', ln=1)
    elif v <= 4 and v > 2:
        pdf.cell(0, 8, 'The score is classified as good, indicating a manageable level of visual complexity', ln=1)
        pdf.cell(0, 8, 'for individuals on the spectrum to differentiate between components with relative ease.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Maintain a balance between visual interest and simplicity to create an engaging yet ', ln=1)
        pdf.cell(0, 8, 'accessible design.', ln=1)
    elif v <= 2 and v >= 0:
        pdf.cell(0, 8, 'The score is classified as very good, indicating minimal visual complexity, making it', ln=1)
        pdf.cell(0, 8, 'easy for individuals on the spectrum to differentiate between components effortlessly.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Strive for a visually pleasing design that remains simple and easy to comprehend.', ln=1)
    elif v == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.ln(10)
    pdf.set_font('times', 'B', 14)
    if t != -1:
        pdf.cell(0, 8, f'Text Complexity score : {f_t}', ln=1)
    else:
        pdf.cell(0, 8, f'Text Complexity score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if t <= 10 and t >= 0:
        pdf.cell(0, 8, 'The score is classified as very good, indicating minimal text complexity, making it', ln=1)
        pdf.cell(0, 8, 'highly accessible and understandable for individuals on the spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Define any special or techincal terms to improve understanding.', ln=1)
    elif t > 10 and t <= 14:
        pdf.cell(0, 8, 'The score is classified as good, indicating a low level of text complexity,', ln=1)
        pdf.cell(0, 8, 'which is generally easy for individuals on the spectrum to comprehend.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Divide complex sentences into seperate sentences.', ln=1)
    elif t > 14 and t < 20:
        pdf.cell(0, 8, 'The score is classified as okay, suggesting a moderate level of text complexity,', ln=1)
        pdf.cell(0, 8, 'which may present some challenges for individuals on the spectrum but remains manageable ',
                 ln=1)
        pdf.cell(0, 8, 'with effort.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Define technical terms and provide necessary informations.', ln=1)
    elif t >= 20 and t <= 30:
        pdf.cell(0, 8, 'The score is classified as bad, indicating a high level of text complexity, which can pose',
                 ln=1)
        pdf.cell(0, 8,
                 'significant difficulties for individuals on the spectrum in understanding and processing the content.',
                 ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Simplify language and sentence structure to make the text more accessible and easier ', ln=1)
        pdf.cell(0, 8, 'to comprehend.', ln=1)
    elif t > 30:
        pdf.cell(0, 8, 'The score is classified as very bad, representing an extremely high level of text complexity,',
                 ln=1)
        pdf.cell(0, 8,
                 'making it nearly impossible for individuals on the spectrum to comprehend the content effectively.',
                 ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Rewrite the text using clear, concise language and shorter sentences to drastically ', ln=1)
        pdf.cell(0, 8, 'reduce complexity.', ln=1)
    elif t == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.ln(10)
    if i != -1:
        pdf.cell(0, 8, f'Image Complexity score : {f_i}', ln=1)
    else:
        pdf.cell(0, 8, f'Image Complexity score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if i <= 0.2 and i >= 0:
        pdf.cell(0, 8, 'The score is classified as very good, indicating minimal visual clutter with clear ', ln=1)
        pdf.cell(0, 8,
                 'outlines and simple shapes, making it highly accessible and comfortable for individuals on the ',
                 ln=1)
        pdf.cell(0, 8, 'spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Ensure that images are appropriately sized to prevent overwhelming the viewer.', ln=1)
    elif i <= 0.4 and i > 0.2:
        pdf.cell(0, 8, 'The score is classified as good, suggesting the use of images with moderate complexity ', ln=1)
        pdf.cell(0, 8,
                 'and a harmonious color palette, providing a visually pleasing experience for individuals on the',
                 ln=1)
        pdf.cell(0, 8, 'spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Choose textures that are gentle and non-distracting.', ln=1)
    elif i <= 0.6 and i > 0.4:
        pdf.cell(0, 8, 'The score is classified as okay, indicating controlled visual elements and a restrained ', ln=1)
        pdf.cell(0, 8, 'color scheme, which may present some challenges for individuals on the spectrum but remains ',
                 ln=1)
        pdf.cell(0, 8, 'manageable with effort.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Opt for textures that are subtle and uniform across the image.', ln=1)
    elif i <= 0.8 and i > 0.6:
        pdf.cell(0, 8, 'The score is classified as bad, suggesting images with excessive details or vibrant colors ',
                 ln=1)
        pdf.cell(0, 8, 'that may overwhelm sensory processing, posing significant difficulties for individuals on the ',
                 ln=1)
        pdf.cell(0, 8, 'spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8,
                 ' : Avoid images with excessive details or intricate patterns that may overwhelm sensory processing,',
                 ln=1)
        pdf.cell(0, 8, 'and minimize the use of vibrant colors or high-contrast combinations.', ln=1)
    elif i > 0.8:
        pdf.cell(0, 8, 'The score is classified as very bad, representing images with high visual complexity and ',
                 ln=1)
        pdf.cell(0, 8, 'sensory stimuli, making it nearly impossible for individuals with autism to process ', ln=1)
        pdf.cell(0, 8, 'effectively and causing significant discomfort.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Use a muted color palette with minimal variation to promote calmness, and opt ', ln=1)
        pdf.cell(0, 8, 'for smooth, uniform textures to minimize sensory discomfort.', ln=1)
    elif i == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.ln(10)
    if r != -1:
        pdf.cell(0, 8, f'Text-Image Ratio score : {f_r}', ln=1)
    else:
        pdf.cell(0, 8, f'Text-Image Ratio score : NA', ln=1)
    pdf.set_font('times', '', 14)
    if r <= 50 and r >= 0:
        pdf.cell(0, 8, 'The ratio is classified as very good, indicating a well-balanced mix of text and images,', ln=1)
        pdf.cell(0, 8, 'providing sufficient visual support and engagement for users on the autism spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Maintain the current balance between text and images, as it provides an optimal mix ', ln=1)
        pdf.cell(0, 8, 'of textual information and visual support.', ln=1)
    elif r <= 100 and r > 50:
        pdf.cell(0, 8, 'The ratio is classified as good, suggesting a slightly higher emphasis on textual ', ln=1)
        pdf.cell(0, 8, 'content but still maintaining a reasonable balance with images, contributing to an overall ',
                 ln=1)
        pdf.cell(0, 8, 'engaging user experience.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Consider increasing the number of images or visual elements slightly to provide additional ',
                 ln=1)
        pdf.cell(0, 8, 'visual support and engagement.', ln=1)
    elif r <= 150 and r > 100:
        pdf.cell(0, 8, 'The ratio is classified as okay, indicating a moderate imbalance between text and images, ',
                 ln=1)
        pdf.cell(0, 8, 'which may present some challenges for users in terms of visual support and engagement.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Ensure that images are used strategically to enhance understanding and engagement.', ln=1)
    elif r <= 200 and r > 150:
        pdf.cell(0, 8, 'The ratio is classified as bad, suggesting a significant imbalance with an excessive ', ln=1)
        pdf.cell(0, 8, 'emphasis on textual content over images, potentially leading to decreased visual ', ln=1)
        pdf.cell(0, 8, 'engagement and accessibility for users.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Decrease the amount of textual content and increase the number of images ', ln=1)
        pdf.cell(0, 8, 'to create a more balanced and engaging user experience.', ln=1)
    elif r <= 250 and r > 200:
        pdf.cell(0, 8, 'The ratio is classified as very bad, indicating an extreme imbalance with an ', ln=1)
        pdf.cell(0, 8, 'overwhelming emphasis on textual content, severely limiting visual support ', ln=1)
        pdf.cell(0, 8, 'and engagement for users on the autism spectrum.', ln=1)
        pdf.set_font('times', 'B', 14)
        pdf.cell(22, 8, 'Suggestion')
        pdf.set_font('times', '', 14)
        pdf.cell(0, 8, ' : Significantly reduce the amount of textual content and substantially increase ', ln=1)
        pdf.cell(0, 8, 'the number of images to create a more visually engaging and accessible user experience,', ln=1)
        pdf.cell(0, 8, 'while also ensuring that images are used strategically to convey information and enhance ',
                 ln=1)
        pdf.cell(0, 8, 'comprehension for users on the autism spectrum.', ln=1)
    elif r == -1:
        pdf.cell(0, 8, 'This metric was not selected during the scan.', ln=1)
    pdf.cell(0, 8, '____________________________________________________________________________', ln=1)
    return pdf


def addtable(urllist, dlist, vlist, tlist, ilist, rlist, totallist, pdf):
    pdf.set_font('times', '', 10)
    column_width = 27
    column_height = 10  # Height of each cell
    column_names = ["URL", "Distinguishibility", "Visual Complexity", "Text Complexity", "Image Complexity",
                    "Text-Image Ratio", "Total Score"]

    # Print column names
    for name in column_names:
        pdf.cell(column_width, column_height, name, border=1, align='C')
    pdf.ln()
    j=0
    # Print data rows
    for i in range(len(urllist)):
        # Calculate the height of URL cell
        url_lines = pdf.multi_cell(column_width, column_height, str(urllist[i]), border=1)
        url_height = len(url_lines) * column_height

        # Print other columns, adjusting their height if necessary
        max_height = max(url_height, column_height)
        pdf.set_xy(column_width + 10, pdf.get_y() - max_height)  # Set position for the first column after URL

        # Print each data element with center alignment and NA instead of -1
        for data in [dlist[i], vlist[i], tlist[i], ilist[i], rlist[i]]:
            if data == -1:
                pdf.cell(column_width, max_height, "NA", border=1, align='C')
            else:
                pdf.cell(column_width, max_height, f"{data:.2f}", border=1, align='C')  # Print with 2 decimal places

        pdf.cell(column_width, max_height, totallist[j], border=1, align='C')
        j+=1
        pdf.ln()

    return pdf
