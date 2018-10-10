# import logging

from flask import request, jsonify

from codeitsuisse import app

# logger = logging.getLogger(__name__)


@app.route('/hardcode', methods=['GET'])
def hardcode():
    # data = request.get_json()
    # app.logger.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    # result = inputValue * inputValue
    # app.logger.info("My result :{}".format(result))

    response = {
        "items": [
            {
                "id": 1,
                "name": "jelly",
                "qty": 2,
                "price": 9.54
            }, {
                "id": 2,
                "name": "peanut",
                "qty": 1,
                "price": 15.24
            }, {
                "id": 3,
                "name": "shampoo",
                "qty": 3,
                "price": 1.00
            }, {
                "id": 4,
                "name": "spam",
                "qty": 1,
                "price": 0.25
            }
        ]
    }
    return jsonify(response)
    # return jsonify(result)


@app.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):

    items = {
        '0001': {
            "id": 1,
            "name": "jelly",
            "qty": 2,
            "price": 9.54
        },
        '0002': {
            "id": 2,
            "name": "peanut",
            "qty": 1,
            "price": 15.24
        },
        '0003': {
            "id": 3,
            "name": "shampoo",
            "qty": 3,
            "price": 1.00
        },
        '0004': {
            "id": 4,
            "name": "spam",
            "qty": 1,
            "price": 0.25
        }
    }

    response = items[item_id]
    return jsonify(response)
