"""
A point can move in nine different directions
1. where point remains its own location where should not consumer
"""
import unittest

from src.execute import calculate_power_required
from src.models import Point


class TestData:
    def __init__(self, source: Point, destination: Point,
                 expected_power_required: int):
        self.source = source
        self.destination = destination
        self.expected_power_required = expected_power_required


testdata_when_source_facing_eastwards = [
    # same place
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=3, y=3),
        expected_power_required=0
    ),
    #  downward
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=3, y=0),
        expected_power_required=35
    ),
    #  upwards
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=3, y=6),
        expected_power_required=35
    ),
    #  forward
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=6, y=3),
        expected_power_required=30
    ),
    #  backward
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=0, y=3),
        expected_power_required=40
    ),
    #  north-west
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=0, y=6),
        expected_power_required=70
    ),
    #  south-west
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=0, y=0),
        expected_power_required=70
    ),
    #  south-east
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=6, y=0),
        expected_power_required=65
    ),
    #  north-east
    TestData(
        source=Point.create(x=3, y=3, direction="E"),
        destination=Point.create(x=6, y=6),
        expected_power_required=65
    ),

]

testdata_when_source_facing_westwards = [
    # same place
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=3, y=3),
        expected_power_required=0
    ),
    #  downward
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=3, y=0),
        expected_power_required=35
    ),
    #  upwards
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=3, y=6),
        expected_power_required=35
    ),
    #  backward
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=6, y=3),
        expected_power_required=40
    ),
    #  forward
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=0, y=3),
        expected_power_required=30
    ),
    #  north-west
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=0, y=6),
        expected_power_required=65
    ),
    #  south-west
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=0, y=0),
        expected_power_required=65
    ),
    #  south-east
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=6, y=0),
        expected_power_required=70
    ),
    #  north-east
    TestData(
        source=Point.create(x=3, y=3, direction="W"),
        destination=Point.create(x=6, y=6),
        expected_power_required=70
    ),

]


class CalculatePowerRequiredTestCase(unittest.TestCase):

    def test_power_required(self):
        for testdata in testdata_when_source_facing_eastwards + testdata_when_source_facing_westwards:
            with self.subTest(msg=f"Testing {testdata}"):
                actual_power_required = calculate_power_required(
                    source=testdata.source,
                    destination=testdata.destination)
                assert actual_power_required == testdata.expected_power_required
