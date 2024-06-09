import unittest
import imageMain as im


class TestCalculateNormalizedEntropy(unittest.TestCase):

    def test_calculate_normalized_entropy_from_url(self):
        image_url = "https://fauziaskitchenfun.com/wp-content/uploads/2017/01/21-1024x765.jpg"

        normalized_entropy = im.calculate_normalized_entropy_from_url(image_url)

        self.assertTrue(0 <= normalized_entropy <= 1)


if __name__ == '__main__':
    unittest.main()
