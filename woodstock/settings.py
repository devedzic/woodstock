"""Project configuration settings (PROJECT_DIR etc.)
"""


import os

# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))

# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(PROJECT_DIR)


from pathlib import Path

PROJECT_DIR = Path(__file__).parent

# PROJECT_DIR = Path.cwd()
# print(PROJECT_DIR)
# DATA_DIR = PROJECT_DIR / 'data'
# print(DATA_DIR)
# print(type(PROJECT_DIR))

