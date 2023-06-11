"""
A point can move in nine different directions
1. where point remains its own location where should not consumer
"""
from dataclasses import dataclass

import pytest

from src.execute import calculate_power_required
from src.models import Point


@dataclass
class TestData:
    source: Point
    destination: Point
    expected_power_required: int
    __test__ = False


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

testdata_when_source_facing_eastwards_ids = [f"{item}" for item in
                                             testdata_when_source_facing_eastwards]

testdata_when_source_facing_westwards_ids = [f"{item}" for item in
                                             testdata_when_source_facing_westwards]


@pytest.fixture(
    params=testdata_when_source_facing_eastwards + testdata_when_source_facing_westwards,
    ids=testdata_when_source_facing_eastwards_ids + testdata_when_source_facing_westwards_ids)
def testdata(request):
    return request.param


def test_power_required(testdata):
    actual_power_required = calculate_power_required(source=testdata.source,
                                                     destination=testdata.destination)
    assert actual_power_required == testdata.expected_power_required


def test_power_required_when():
    data = TestData(
        source=Point.create(x=0, y=0, direction="w"),
        destination=Point.create(x=6, y=6),
        expected_power_required=130
    )
    actual_power_required = calculate_power_required(source=data.source,
                                                     destination=data.destination)
    assert actual_power_required == data.expected_power_required
