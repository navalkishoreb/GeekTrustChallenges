import os.path
from typing import Union
import unittest

from src.execute import calculate_power, parse_input_file
from src.models import Point, Command
from tests import logger


def get_output_from_file(output_file: str) -> Union[str, None]:
    try:
        with open(output_file) as data:
            output_data = next(data).strip()
            return output_data
    except FileNotFoundError as err:
        logger.error(err)
        return None


samples = ["sample1", "sample2", "sample3"]


class EndToEndTestCase(unittest.TestCase):

    def test_calculate_power(self):
        for item in samples:
            with self.subTest(msg=f"testing {item}"):
                parent_directory = os.path.dirname(os.path.realpath(__file__))
                sample_directory = os.path.join(parent_directory, "resources",
                                                item)
                input_file = os.path.join(sample_directory, "input.txt")
                output_file = os.path.join(sample_directory, "output.txt")
                actual_power = calculate_power(input_file=input_file)
                expected_power = get_output_from_file(output_file=output_file)
                assert actual_power == expected_power


class FileOperationTestCase(unittest.TestCase):

    def test_parse_input_file(self):
        parent_directory = os.path.dirname(os.path.realpath(__file__))
        sample_directory = os.path.join(parent_directory, "resources",
                                        "sample1")
        input_file = os.path.join(sample_directory, "input.txt")
        source, destination, command = parse_input_file(input_file=input_file)
        expected_source = Point.create(x=2, y=1, direction="E")
        expected_destination = Point.create(x=4, y=3)
        expected_command = Command.PRINT_POWER
        assert (source, destination, command) == (
            expected_source, expected_destination, expected_command)
