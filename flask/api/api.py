from flask import Flask
from flask_restx import Api, Resource
from flask import request, Response
from pymongo import MongoClient
from werkzeug.datastructures import FileStorage
from itertools import combinations
from random import random, sample, seed
from datetime import datetime
from PIL import Image
from pprint import pprint
import json
import os
import io

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://mongo:27017')
db = client.core

seed(random())

class BoundingBox:
    def __init__(self, data):
        self.x1: float = data["x1"]
        self.y1: float = data["y1"]
        self.x_off: float = data["x_off"]
        self.y_off: float = data["y_off"]

    def check_for_OSIA(self):
        if (self.x1 + self.x_off > 1 or self.y1 + self.y_off > 1 or self.x1 < 0 or self.y1 < 0):
            return True

        return False

    def get_box(self):
        return {"x1": self.x1, "y1": self.y1, "x_off": self.x_off, "y_off": self.y_off}

    def intersects(self, other):
        dx = min(self.x1 + self.x_off, other.x1 + other.x_off) - max(self.x1, other.x1)
        dy = min(self.y1 + self.y_off, other.y1 + other.y_off) - max(self.y1, other.y1)

        if (dx >= 0 and dy >= 0):
            return True
        else:
            return False

def generate_box_data(data_file, count = 3):
    boxes = []
    data = None

    data = json.load(data_file)

    data = sample(data, count)

    for d in data:
        box = BoundingBox(d)
        box.check_for_OSIA()
        boxes.append(box)
    
    return boxes

def store_data(image, data):
    cv = {"image": image.getvalue()}

    cv["bounding_boxes"] = data["boxes"]
    cv["errors"] = data["errors"]
    cv["timestamp"] = datetime.utcnow()

    cvs = db.cvs
    cv_id = cvs.insert_one(cv).inserted_id

def check_intersections(boxes):
    overlapping_indexes = []
    for box1, box2 in combinations(boxes, 2):
        if box1.intersects(box2):
            if (boxes.index(box1) not in overlapping_indexes):
                overlapping_indexes.append(boxes.index(box1))
            if (boxes.index(box2) not in overlapping_indexes):
                overlapping_indexes.append(boxes.index(box2))

    return overlapping_indexes

@api.route('/runcv', methods=['POST'])
class parse_cv(Resource):
    def post(self):
        img = Image.open(request.files.get('file'))
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')

        with open("sample-data.json", "r") as f:
            boxes = generate_box_data(data_file = f)

        r = {"boxes": [box.get_box() for box in boxes], "errors": []}

        r["errors"].append({"type": "OutsideImageArea", "boxIndexes": [ind for ind, b in enumerate(boxes) if b.check_for_OSIA()]})

        r["errors"].append({"type": "overlap", "boxIndexes": check_intersections(boxes)})

        store_data(img_bytes, r)

        return Response(json.dumps(r), status=200, mimetype="application/json")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
