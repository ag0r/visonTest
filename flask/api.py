from flask import Flask, Response
from flask_restx import Api, Resource
from flask import request
from pymongo import MongoClient
import os

app = Flask(__name__)
api = Api(app)

client = MongoClient()

@api.route('/runcv', methods=['POST', 'GET'])
class parse_cv(Resource):
    def post(self):
        print(request.files, flush=True)
        cv = {
        "x1": 0.30,
        "y1": 0.47,
        "x_off": 0.334,
        "y_off": 0.34
        }

        return Response(cv, status=200, mimetype='application/json')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
