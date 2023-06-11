from dataclasses import asdict

import pytest

from src.models import Point, Direction


def test_models_point():
    point = Point(x=2, y=2, direction=Direction.EAST.value)
    point_as_dict = asdict(point)
    expected_dict = dict(x=2, y=2, direction="E")
    assert point_as_dict == expected_dict


def test_models_point_create():
    point = Point.create(x=2, y=2, direction=Direction.EAST.value)
    point_as_dict = asdict(point)
    expected_dict = dict(x=2, y=2, direction="E")
    assert point_as_dict == expected_dict


def test_models_point_when_point_outside_boundary():
    with pytest.raises(Point.PointOutsideBoundary):
        Point.create(x=7, y=7, direction=Direction.EAST.value)
