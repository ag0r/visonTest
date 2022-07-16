from api.api import BoundingBox
import unittest


class TestBoundingBox(unittest.TestCase):
    def test_get_box(self):
        data1 = {"x1": 0.1, "y1": 0.1, "x_off": 0.1, "y_off": 0.1}
        data2 = {"x1": 0.2, "y1": 0.2, "x_off": 0.2, "y_off": 0.2}

        box = BoundingBox(data1)

        self.assertEqual(data1, box.get_box())
        self.assertNotEqual(data2, box.get_box())

    def test_OSIA(self):
        """
        Test that outside image area checks work
        """

        data = {
            "x1": 0.1,
            "y1": 0.1,
            "x_off": 0.1,
            "y_off": 0.1
            }

        box = BoundingBox(data)
        self.assertFalse(box.check_for_OSIA())

        data = {
            "x1": 0.5,
            "y1": 0.1,
            "x_off": 0.6,
            "y_off": 0.1
            }

        box = BoundingBox(data)
        self.assertTrue(box.check_for_OSIA())

        data = {
            "x1": 0.1,
            "y1": 0.5,
            "x_off": 0.1,
            "y_off": 0.6
            }

        box = BoundingBox(data)
        self.assertTrue(box.check_for_OSIA())

        data = {
            "x1": 1.1,
            "y1": 0.1,
            "x_off": 0.1,
            "y_off": 0.1
            }

        box = BoundingBox(data)
        self.assertTrue(box.check_for_OSIA())

        data = {
            "x1": 0.1,
            "y1": 1.1,
            "x_off": 0.1,
            "y_off": 0.1
            }

        box = BoundingBox(data)
        self.assertTrue(box.check_for_OSIA())

        data = {
            "x1": -0.5,
            "y1": 0.1,
            "x_off": 0.1,
            "y_off": 0.1
            }

        box = BoundingBox(data)
        self.assertTrue(box.check_for_OSIA())

        data = {
            "x1": 0.1,
            "y1": -0.5,
            "x_off": 0.1,
            "y_off": 0.1
            }

        box = BoundingBox(data)
        self.assertTrue(box.check_for_OSIA())

    def test_inersects(self):
        box1 = BoundingBox({"x1": 0.1, "y1": 0.1, "x_off": 0.5, "y_off": 0.5})
        box2 = BoundingBox({"x1": 0.2, "y1": 0.2, "x_off": 0.2, "y_off": 0.2})

        self.assertTrue(box1.intersects(box2))
        self.assertTrue(box2.intersects(box1))

        box1 = BoundingBox({"x1": 0.1, "y1": 0.1, "x_off": 0.5, "y_off": 0.5})
        box2 = BoundingBox({"x1": 0.7, "y1": 0.7, "x_off": 0.1, "y_off": 0.1})

        self.assertFalse(box1.intersects(box2))
        self.assertFalse(box2.intersects(box1))

if __name__ == '__main__':
    unittest.main()
