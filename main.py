from flask import Flask, jsonify, request
import beer_controller
from db import create_tables
import argparse

app = Flask(__name__)


@app.route('/beer', methods=["GET"])
def get_beers():
    beers = beer_controller.get_beers()
    return jsonify(beers)


@app.route("/beer", methods=["POST"])
def insert_beer():
    beer_details = request.get_json()

    date = beer_details.get('date', None)
    defendant = beer_details.get('defendant', 1)
    defendant_id = beer_details.get('defendant_id', 0)
    prosecutors = beer_details.get('prosecutors', None)
    description = beer_details.get('description', None)
    count = beer_details.get('count', 1)

    result = beer_controller.insert_beer(date, defendant, defendant_id, prosecutors, description, count)
    return jsonify(result)


@app.route("/beer/<id>", methods=["PUT"])
def update_beer(id):
    beer_details = request.get_json()

    date = beer_details.get('date', None)
    defendant = beer_details.get('defendant', 1)
    defendant_id = beer_details.get('defendant_id', 0)
    prosecutors = beer_details.get('prosecutors', None)
    description = beer_details.get('description', None)
    count = beer_details.get('count', 1)

    result = beer_controller.update_beer(id, date, defendant, defendant_id, prosecutors, description, count)
    return jsonify(result)


@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, " \
                                          "Authorization "
    return response


if __name__ == "__main__":
    create_tables()

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Port", type=int, default=8000)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.p, debug=False)
