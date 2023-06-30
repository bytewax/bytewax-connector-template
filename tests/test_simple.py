import unittest

# from sample.sample_input_connector import SampleInput


class TestSimple(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(5 + 1, 6)


if __name__ == "__main__":
    unittest.main()
