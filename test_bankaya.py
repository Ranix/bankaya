import unittest

from bankaya import open_file, strig_to_ascii


class TestOccurrence(unittest.TestCase):

    def setUp(self):
        # Load test data
        self.bug = strig_to_ascii('bug.txt', open_file)
        self.landscape = strig_to_ascii('landscape.txt', open_file)

    def test_occurrence(self):
        self.assertEqual(self.landscape.count(self.bug), 3, "Should be 3")

if __name__ == '__main__':
    unittest.main()