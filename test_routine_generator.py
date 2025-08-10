import unittest
from unittest.mock import patch
from routine_generator import generate_routine

class TestGenerateRoutine(unittest.TestCase):
    @patch("routine_generator.client.chat.completions.create")
    def test_generate_routine_success(self, mock_create):
        # Mock the API response
        mock_create.return_value = type("Response", (object,), {
            "choices": [
                type("Choice", (object,), {
                    "message": type("Message", (object,), {
                        "content": "Rutina generada correctamente."
                    })
                })
            ]
        })()

        # Call the function
        result = generate_routine("ganar músculo", "principiante")

        # Assert the result
        self.assertEqual(result, "Rutina generada correctamente.")

    @patch("routine_generator.client.chat.completions.create")
    def test_generate_routine_encoding_error(self, mock_create):
        # Simulate an encoding error
        mock_create.side_effect = UnicodeEncodeError("utf-8", "test", 0, 1, "reason")

        # Assert that the function raises a ValueError
        with self.assertRaises(ValueError) as context:
            generate_routine("ganar músculo", "principiante")
        self.assertIn("Encoding error", str(context.exception))

    @patch("routine_generator.client.chat.completions.create")
    def test_generate_routine_unexpected_error(self, mock_create):
        # Simulate a generic exception
        mock_create.side_effect = Exception("Unexpected API error")

        # Assert that the function raises a ValueError
        with self.assertRaises(ValueError) as context:
            generate_routine("ganar músculo", "principiante")
        self.assertIn("Unexpected error", str(context.exception))

if __name__ == "__main__":
    unittest.main()