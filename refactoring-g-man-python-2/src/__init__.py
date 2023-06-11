"""
To avail all modules declared in `src` directory
add the parent directory to sys path
"""

import os
import sys

parent_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_directory)
