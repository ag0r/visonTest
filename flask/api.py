from flask import Flask
from flask_restx import Api, Resource
from flask import request, Response
from pymongo import MongoClient
from werkzeug.datastructures import FileStorage
import json
import os
from itertools import combinations
from random import random, sample, seed
from pprint import pprint

app = Flask(__name__)
api = Api(app)

client = MongoClient()

seed(random())

class BoundingBox:
    def __init__(self, data):
        self.x1: float = data["x1"]
        self.y1: float = data["y1"]
        self.x_off: float = data["x_off"]
        self.y_off: float = data["y_off"]

        self.OSIA = False

    def check_for_OSIA(self):
        if (self.x1 + self.x_off > 1 or self.y1 + self.y_off > 1):
            self.OSIA = True

    def get_box(self):
        return {"x1": self.x1, "y1": self.y1, "x_off": self.x_off, "y_off": self.y_off}

    def get_errors(self):
        return self.errors

    def intersects(self, other):
        dx = min(self.x1 + self.x_off, other.x1 + other.x_off) - max(self.x1, other.x1)
        dy = min(self.y1 + self.y_off, other.y1 + other.y_off) - max(self.y1, other.y1)

        if (dx >= 0 and dy >= 0):
            return True
        else:
            return False

def generate_box_data(count = 1):
    boxes = []
    data = None

    with open("sample-data.json", "r") as f:
        data = json.load(f)

    data = sample(data, count)

    for d in data:
        box = BoundingBox(d)
        box.check_for_OSIA()
        boxes.append(box)
    
    return boxes

@api.route('/runcv', methods=['POST'])
class parse_cv(Resource):

    def post(self):
        img = request.files

        boxes = generate_box_data(count = 3)
        r = {"boxes": [box.get_box() for box in boxes], "errors": []}

        r["errors"].append({"type": "OutsideImageArea", "boxIndexes": [ind for ind, b in enumerate(boxes) if b.OSIA]})

        overlapping_indexes = []
        for box1, box2 in combinations(boxes, 2):
            if box1.intersects(box2):
                if (boxes.index(box1) not in overlapping_indexes):
                    overlapping_indexes.append(boxes.index(box1))
                if (boxes.index(box2) not in overlapping_indexes):
                    overlapping_indexes.append(boxes.index(box2))

        r["errors"].append({"type": "overlap", "boxIndexes": overlapping_indexes})

        pprint(r)
        print(flush=True)

        return Response(json.dumps(r), status=200, mimetype="application/json")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
