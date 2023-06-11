from src.models import Point, Direction
import unittest


class PointModelTestCase(unittest.TestCase):

    def test_models_point(self):
        point = Point(x=2, y=2, direction=Direction.EAST.value)
        point_as_dict = point.to_dict()
        expected_dict = dict(x=2, y=2, direction="E")
        assert point_as_dict == expected_dict

    def test_models_point_create(self):
        point = Point.create(x=2, y=2, direction=Direction.EAST.value)
        point_as_dict = point.to_dict()
        expected_dict = dict(x=2, y=2, direction="E")
        assert point_as_dict == expected_dict

    def test_models_point_when_point_outside_boundary(self):
        with self.assertRaises(expected_exception=Point.PointOutsideBoundary):
            Point.create(x=7, y=7, direction=Direction.EAST.value)
