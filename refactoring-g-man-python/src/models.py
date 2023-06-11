from dataclasses import dataclass
from enum import Enum
from typing import Optional

from typing_extensions import Self


class Direction(Enum):
    UNKNOWN = ""
    EAST = "E"
    WEST = "W"
    NORTH = "N"
    SOUTH = "S"

    @classmethod
    def get_enum_from_value(cls, direction_value: str) -> Self:
        try:
            direction_enum = Direction(direction_value)
        except ValueError as e:
            direction_enum = Direction.UNKNOWN
        return direction_enum


@dataclass
class Point:
    x: int
    y: int
    direction: Optional[str] = Direction.UNKNOWN.value

    class PointOutsideBoundary(Exception):
        pass

    MAX_BOUNDARY = 6
    MIN_BOUNDARY = 0

    def __post_init__(self):
        assert isinstance(self.x, int)
        assert isinstance(self.y, int)
        assert isinstance(self.direction, str)
        if (
                self.x > Point.MAX_BOUNDARY
                or self.y > Point.MAX_BOUNDARY
                or self.x < Point.MIN_BOUNDARY
                or self.y < Point.MIN_BOUNDARY
        ):
            raise Point.PointOutsideBoundary(f"{self !r}")

    @classmethod
    def is_source_point(cls, opcode):
        return opcode == "SOURCE"

    @classmethod
    def is_destination_point(cls, opcode):
        return opcode == "DESTINATION"

    @classmethod
    def create(cls, x, y, direction: Optional[str] = ""):
        """
        Assert all datatypes
        x and y should be able to convert to integer datatype
        Create Point from given values
        :param x:
        :param y:
        :param direction:
        :return:
        """
        int_x = int(x)
        int_y = int(y)
        direction_enum = Direction.get_enum_from_value(direction)
        return Point(x=int_x, y=int_y, direction=direction_enum.value)


class Command(Enum):
    PRINT_POWER = "PRINT_POWER"

    @classmethod
    def is_valid_command(cls, opcode):
        return opcode in Command.__members__


def get_movement_in_vertical(diff_vertical):
    if not abs(diff_vertical):
        return ""
    if diff_vertical < 0:
        return Direction.SOUTH.value
    else:
        return Direction.NORTH.value


def get_movement_in_horizontal(diff_horizontal):
    if not abs(diff_horizontal):
        return ""
    if diff_horizontal < 0:
        return Direction.WEST.value
    else:
        return Direction.EAST.value


def get_vertical_turn(diff_horizontal):
    if not abs(diff_horizontal):
        return ""
    if diff_horizontal < 0:
        return Direction.WEST.value
    else:
        return Direction.EAST.value


def get_number_of_turns(diff_horizontal, diff_vertical,
                        initial_direction) -> int:
    movement_in_vertical = get_movement_in_vertical(diff_vertical)
    movement_in_horizontal = get_movement_in_horizontal(diff_horizontal)

    if not movement_in_vertical and not movement_in_horizontal:
        return 0
    if movement_in_vertical and not movement_in_horizontal:
        if movement_in_vertical == initial_direction:
            return 0
        elif initial_direction in ["W", "E"]:
            return 1
        else:
            return 2
    if not movement_in_vertical and movement_in_horizontal:
        if movement_in_horizontal == initial_direction:
            return 0
        elif initial_direction in ["N", "S"]:
            return 1
        else:
            return 2
    if initial_direction in [movement_in_vertical, movement_in_horizontal]:
        return 1
    return 2
