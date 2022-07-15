from flask import Flask
from flask_restx import Api, Resource
from flask import request, Response
from pymongo import MongoClient
from werkzeug.datastructures import FileStorage
import json
import os
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

        self.errors = []

    def check_for_errors(self):
        if (self.x_off < self.x1 or self.y_off < self.y1):
            print(self.get_box(), flush=True)
            self.errors.append("overlap")

        if (self.x1 + self.x_off > 1 or self.y1 + self.y_off > 1 or self.x1 - self.x_off < 0 or self.y1 - self.y_off < 0):
            self.errors.append("OutsideImageArea")

    def get_box(self):
        return {"x1": self.x1, "y1": self.y1, "x_off": self.x_off, "y_off": self.y_off}

    def get_errors(self):
        return self.errors

def generate_box_data(count = 1):
    boxes = []
    data = None

    with open("sample-data.json", "r") as f:
        data = json.load(f)

    data = sample(data, count)

    for d in data:
        box = BoundingBox(d)
        box.check_for_errors()
        boxes.append(box)
    
    return boxes

@api.route('/runcv', methods=['POST'])
class parse_cv(Resource):

    def post(self):
        print(request.files)

        boxes = generate_box_data(count = 3)
        r = {"boxes": [box.get_box() for box in boxes], "errors": []}

        for error in ["OutsideImageArea", "overlap"]:
            r["errors"].append({"type": error, "boxIndexes": [ind for ind, b in enumerate(boxes) if error in b.get_errors()]})

        pprint(r)
        print(flush=True)

#        r = {
#          "boxes": [
#            {
#              "x1": 0.30,
#              "y1": 0.47,
#              "x_off": 0.334,
#              "y_off": 0.34
#            }
#          ],
#          "errors": [
#            {
#              "type": "overlap",
#              "boxIndexes": [0]
#            }
#          ]
#        }

        return Response(json.dumps(r), status=200, mimetype="application/json")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
