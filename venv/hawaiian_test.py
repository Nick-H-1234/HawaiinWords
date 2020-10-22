import unittest
from hawaiian_words import translate

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(["Ah-loh-hah"], translate("aloha"))


if __name__ == '__main__':
    unittest.main()
