"""
Assumptions
 The grid is 6 X 6. All coordinates will have values between 0 - 6.
 Direction value can either be N, E, W or S.
 There could be multiple paths from source to destination.
 G-Man will spend the least amount of power to reach the destination.
 All the destination paths will be on the grid.
 Only the final coordinates of the destination need to be considered.
 There is no need to consider the direction of the destination.
"""

import argparse
from src.execute import calculate_power


def main(input_file: str):
    output = calculate_power(input_file)
    print(f"{output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate remaining power")
    parser.add_argument("input_file",
                        help="Provide sample input file")
    args = parser.parse_args()
    main(input_file=args.input_file)
