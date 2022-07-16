from api.api import BoundingBox, generate_box_data
import unittest
import unittest.mock as um
import json


class TestGenerateBoxData(unittest.TestCase):
    def test_generate_box_data(self):
        test_data = [
            {
              "x1": 0.25,
              "y1": 0.25,
              "x_off": 0.1,
              "y_off": 0.1
            },
            {
              "x1": 0.5,
              "y1": 0.27,
              "x_off": 0.2,
              "y_off": 0.15
            },
            {
              "x1": 0.38,
              "y1": 0.535,
              "x_off": 0.2,
              "y_off": 0.05
            },
            {
              "x1": 0.31,
              "y1": 0.28,
              "x_off": 0.1,
              "y_off": 0.1
            },
            {
              "x1": 0.5,
              "y1": 0.27,
              "x_off": 0.64,
              "y_off": 0.15
            },
            {
              "x1": 0.30,
              "y1": 0.47,
              "x_off": 0.334,
              "y_off": 0.34
            }
          ]

        with um.patch('builtins.open', um.mock_open(read_data=json.dumps(test_data))):
            with open('/dev/null') as f:
                boxes = generate_box_data(data_file = f)

                self.assertEqual(len(boxes), 3)

if __name__ == '__main__':
    unittest.main()
