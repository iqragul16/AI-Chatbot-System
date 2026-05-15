import unittest
from chatbot import get_response


class TestChatbot(unittest.TestCase):

    def test_hello(self):
        self.assertIn(get_response("hello"), ["Hi!", "Hello!", "Hey there!"])

    def test_python(self):
        self.assertEqual(
            get_response("python"),
            "Python is a programming language."
        )

    def test_ai(self):
        self.assertEqual(
            get_response("ai"),
            "AI stands for Artificial Intelligence."
        )

    def test_machine_learning(self):
        self.assertEqual(
            get_response("what is machine learning"),
            "Machine Learning is a branch of AI that learns from data."
        )

    def test_data_science(self):
        self.assertEqual(
            get_response("what is data science"),
            "Data Science is the study of data to extract insights."
        )

    def test_empty(self):
        self.assertEqual(
            get_response(""),
            "Please type something."
        )


if __name__ == "__main__":
    unittest.main()