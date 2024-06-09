import unittest
import requests
import imageText as it


class TestCalculateImageTextRatio(unittest.TestCase):

    def test_calculate_image_text_ratio(self):
        urls = ['http://localhost/test1.html', 'http://localhost/test2.html', 'http://localhost/test3.html']
        expected_ratio = [4.50, 5.33, 5.00]
        for url, expected in zip(urls, expected_ratio):
            with self.subTest(url=url):  # Subtest for each URL
                response = requests.get(url)
                ratio = it.calculate_image_text_ratio(response)
                self.assertAlmostEqual(ratio, expected, delta=0.10)
                self.assertGreaterEqual(ratio, 0)  # Assert ratio is greater than or equal to 0
                self.assertLessEqual(ratio, 1000)  # Assert ratio is less than or equal to 1000


if __name__ == '__main__':
    unittest.main()

