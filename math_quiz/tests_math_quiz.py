import unittest
from math_quiz.math_quiz import get_random_integer, get_random_operator, evaluate_expression

class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if the random operator is always one of +, -, *
        for _ in range(1000):  # Testing a large number of random values
            operator = get_random_operator()
            self.assertIn(operator, ['+', '-', '*'])  # Ensure the operator is one of these three


    def test_evaluate_expression(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 4, '-', '3 - 4', -1),  # Added more test cases
            (6, 3, '*', '6 * 3', 18)   # Another example
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # Call the function you're testing (for example, evaluate_expression)
            problem, answer = evaluate_expression(num1, num2, operator)

            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
