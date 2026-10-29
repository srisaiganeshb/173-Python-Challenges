# conftest.py
import sys
import os

# Adds your project root to Python's system path so tests can easily import your main files
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))