from api.api import BoundingBox, check_intersections
import unittest

class TestCheckIntersections(unittest.TestCase):
    def test_check_intersections(self):
        box1 = BoundingBox({"x1": 0.25, "y1": 0.25, "x_off": 0.1, "y_off": 0.1})
        box2 = BoundingBox({"x1": 0.25, "y1": 0.25, "x_off": 0.1, "y_off": 0.1})
        box3 = BoundingBox({"x1": 0.5, "y1": 0.5, "x_off": 0.1, "y_off": 0.1})
        overlapping_boxes = [box1, box2, box3]
        self.assertEquals([0, 1], check_intersections(overlapping_boxes))

        box1 = BoundingBox({"x1": 0.5, "y1": 0.5, "x_off": 0.1, "y_off": 0.1})
        box2 = BoundingBox({"x1": 0.25, "y1": 0.25, "x_off": 0.1, "y_off": 0.1})
        box3 = BoundingBox({"x1": 0.5, "y1": 0.5, "x_off": 0.1, "y_off": 0.1})
        overlapping_boxes = [box1, box2, box3]
        self.assertEquals([0, 2], check_intersections(overlapping_boxes))

        box1 = BoundingBox({"x1": 0.25, "y1": 0.25, "x_off": 0.1, "y_off": 0.1})
        box2 = BoundingBox({"x1": 0.5, "y1": 0.5, "x_off": 0.1, "y_off": 0.1})
        box3 = BoundingBox({"x1": 0.5, "y1": 0.5, "x_off": 0.1, "y_off": 0.1})
        overlapping_boxes = [box1, box2, box3]
        self.assertEquals([1, 2], check_intersections(overlapping_boxes))

        box1 = BoundingBox({"x1": 0.1, "y1": 0.1, "x_off": 0.1, "y_off": 0.1})
        box2 = BoundingBox({"x1": 0.4, "y1": 0.4, "x_off": 0.1, "y_off": 0.1})
        box3 = BoundingBox({"x1": 0.7, "y1": 0.7, "x_off": 0.1, "y_off": 0.1})
        overlapping_boxes = [box1, box2, box3]
        self.assertEquals([], check_intersections(overlapping_boxes))
if __name__ == '__main__':
    unittest.main()
