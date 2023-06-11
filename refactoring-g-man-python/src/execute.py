from typing import Tuple, Optional, List

from src.constants import REQUIRED_POWER_FOR_STEP, REQUIRED_POWER_FOR_TURN, \
    INITIAL_POWER
from src.models import Point, Command, get_number_of_turns


def parse_source_location(tokens: List[str]) -> Optional[Point]:
    _, x, y, direction = tokens
    point = Point.create(x=x, y=y, direction=direction)
    return point


def parse_destination_location(tokens: List[str]) -> Optional[Point]:
    _, x, y = tokens
    point = Point.create(x=x, y=y)
    return point


def parse_action(opcode: str) -> Optional[Command]:
    return Command.__members__.get(opcode)


def parse_input_file(input_file: str) -> Tuple[
    Optional[Point], Optional[Point], Optional[Command]]:
    """
    Parse the input file to generate
    source, destination and command action
    :param input_file:
    :return:
    """
    source = None
    destination = None
    action = None

    with open(input_file) as data:
        for instruction in data.readlines():
            tokens = instruction.split()
            opcode = tokens[0]
            if Point.is_source_point(opcode=opcode):
                source = parse_source_location(tokens)
            if Point.is_destination_point(opcode=opcode):
                destination = parse_destination_location(tokens)
            if Command.is_valid_command(opcode=opcode):
                action = parse_action(opcode=opcode)

    return source, destination, action


def calculate_power_required(source: Point, destination: Point) -> int:
    """
    Count steps and turns required
    Multiply with respective power consumptions
    Return power required to move to destination
    :param source:
    :param destination:
    :return:
    """
    diff_horizontal = destination.x - source.x
    diff_vertical = destination.y - source.y
    x_steps = abs(diff_horizontal)
    y_steps = abs(diff_vertical)

    steps = x_steps + y_steps
    turns = get_number_of_turns(diff_horizontal, diff_vertical,
                                source.direction)

    power_required = (steps * REQUIRED_POWER_FOR_STEP) + (
            turns * REQUIRED_POWER_FOR_TURN)
    return power_required


def calculate_power(input_file: str) -> str:
    """
    Read the input sample
    Traverse the direction mentioned
    Evaluate remaining power
    :param input_file:
    :return: Power remained
    """
    power_template = f"POWER {{}}"
    power_consumed = ""
    source, destination, action = parse_input_file(input_file=input_file)
    if action == Command.PRINT_POWER:
        power_required = calculate_power_required(source=source,
                                                  destination=destination)
        power_consumed = INITIAL_POWER - power_required

    return power_template.format(power_consumed)
