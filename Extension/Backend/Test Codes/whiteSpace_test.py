import unittest
import whiteSpace as ws


class TestCalculateDistinguishability(unittest.TestCase):

    def test_calculate_Distinguishability(self):
        urls = ['https://www.autism.org', 'https://www.autismspeaks.org', 'https://www.cambridgeenglish.org/',
                'https://www.daraz.pk', 'https://www.dawn.com', 'https://www.deakin.edu.au',
                'https://fauziaskitchenfun.com', 'https://www.metu.edu.tr', 'https://www.ncc.metu.edu.tr',
                'https://en.wikipedia.org/wiki/Pakistan']
        expected_ratio = [0.82,0.90,0.74,0.93,0.68,0.68,0.66,0.62,0.61,0.68]
        for url, expected in zip(urls, expected_ratio):
            with self.subTest(url=url):  # Subtest for each URL
                ratio = ws.vicramcalc('',url)
                self.assertAlmostEqual(ratio, expected, delta=0.10)
                self.assertGreaterEqual(ratio, 0)  # Assert ratio is greater than or equal to 0
                self.assertLessEqual(ratio, 10)  # Assert ratio is less than or equal to 1000


if __name__ == '__main__':
    unittest.main()
