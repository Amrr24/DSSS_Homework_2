import random

def get_random_integer(min_value, max_value):
    """
    Generates a random integer between the given min_value and max_value (inclusive).
    
    Parameters:
    - min_value (int): The minimum value for the random number.
    - max_value (int): The maximum value for the random number.

    Returns:
    - int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_operator():
    """
    Randomly selects an arithmetic operator ('+', '-', or '*').

    Returns:
    - str: A random operator.
    """
    return random.choice(['+', '-', '*'])


def evaluate_expression(n1, n2, operator):
    """
    Evaluates a mathematical expression with two numbers and an operator.
    
    Parameters:
    - n1 (int): The first number in the expression.
    - n2 (int): The second number in the expression.
    - operator (str): The arithmetic operator to use ('+', '-', or '*').

    Returns:
    - tuple: A tuple containing the string representation of the problem and the correct answer.
    """
    problem = f"{n1} {operator} {n2}"
    
    # Perform calculation based on the operator
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    
    return problem, answer


def math_quiz():
    score = 0
    total_questions = 5  # Change to a realistic number of questions for the game.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the number of questions
    for _ in range(total_questions):
        # Generate random numbers and operator
        n1 = get_random_integer(1, 10)
        n2 = get_random_integer(1, 10)  # Made the range a whole number to match math operations
        operator = get_random_operator()

        # Get the problem and answer
        problem, correct_answer = evaluate_expression(n1, n2, operator)

        print(f"\nQuestion: {problem}")
        
        while True:  # Input validation loop
            try:
                user_answer = int(input("Your answer: "))
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


# Run the quiz if this script is executed directly
if __name__ == "__main__":
    math_quiz()
