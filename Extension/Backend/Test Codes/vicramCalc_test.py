import unittest
import vicramCalc as vc


class TestCalculateVisualComplexity(unittest.TestCase):

    def test_calculate_visual_complexity(self):
        # urls = ['https://www.autism.org', 'https://www.autismspeaks.org', 'https://www.cambridgeenglish.org/',
        #         'https://www.daraz.pk', 'https://www.dawn.com', 'https://www.deakin.edu.au',
        #         'https://fauziaskitchenfun.com', 'https://www.metu.edu.tr', 'https://www.ncc.metu.edu.tr',
        #         'https://en.wikipedia.org/wiki/Pakistan']
        # expected_ratio = [5.20, 6.38, 9.08, 10.00, 10.00, 10.00, 2.48, 4.68, 3.60, 10.00]
        urls = ['https://localhost/test1.html', 'https://localhost/test2.html', 'https://localhost/test3.html']
        expected_ratio = [5.20, 6.38, 9.08]
        for url, expected in zip(urls, expected_ratio):
            with self.subTest(url=url):  # Subtest for each URL
                ratio = vc.vicramcalc1('', url)
                self.assertAlmostEqual(ratio, expected, delta=0.10)
                self.assertGreaterEqual(ratio, 0)  # Assert ratio is greater than or equal to 0
                self.assertLessEqual(ratio, 10)  # Assert ratio is less than or equal to 1000


if __name__ == '__main__':
    unittest.main()
