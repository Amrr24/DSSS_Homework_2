from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Name of the package
    version='0.1',  # Version of your package
    packages=find_packages(),  # Automatically finds and includes your math_quiz folder
    install_requires=[  # List of dependencies (none for now)
        # 'some_package',
    ],
    entry_points={  # The command line entry point for your math_quiz script
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Points to the math_quiz function in math_quiz.py
        ],
    },
)
