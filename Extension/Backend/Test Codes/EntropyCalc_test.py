import unittest
import requests
import EntropyCalc as im


class TestCalculateImageComplexity(unittest.TestCase):

    def test_calculate_image_complexity(self):
        screen_size = (1536,864)
        urls = ['https://www.autism.org', 'https://www.autismspeaks.org', 'https://www.cambridgeenglish.org/',
                'https://www.daraz.pk', 'https://www.dawn.com', 'https://www.deakin.edu.au',
                'https://fauziaskitchenfun.com', 'https://www.metu.edu.tr', 'https://www.ncc.metu.edu.tr',
                'https://en.wikipedia.org/wiki/Pakistan']
        expected_ratio = [0.69, 0.87, 0.58, 0.66, 0.84, 0.92, 0.93, 0.55, 0.79, 0.78]
        for url, expected in zip(urls, expected_ratio):
            with self.subTest(url=url):  # Subtest for each URL
                response = requests.get(url)
                ratio = im.calculate_image_complexity(response, url, screen_size)
                self.assertAlmostEqual(ratio, expected, delta=0.10)
                self.assertGreaterEqual(ratio, 0)  # Assert ratio is greater than or equal to 0
                self.assertLessEqual(ratio, 1)  # Assert ratio is less than or equal to 1000


if __name__ == '__main__':
    unittest.main()

