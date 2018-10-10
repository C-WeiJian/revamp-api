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
            "price": 9.54,
            "description": "wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "http://blog.partypieces.co.uk/wp-content/uploads/2015/01/jan-2015-pineapplejelly.jpg"
        },
        '0002': {
            "id": 2,
            "name": "peanut",
            "price": 15.24,
            "description": "wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "https://www.sciencenews.org/sites/default/files/styles/growth_curve_main/public/2017/01/main/blogposts/011317_MR_peanut-allergies_main.jpg?itok=c8zS79Sb"
        },
        '0003': {
            "id": 3,
            "name": "shampoo",
            "price": 1.00,
            "description": "wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "https://images-na.ssl-images-amazon.com/images/I/716GPlRZ23L._SL1500_.jpg"
        },
        '0004': {
            "id": 4,
            "name": "spam",
            "price": 0.25,
            "description": "wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Spam_can.png/220px-Spam_can.png"
        }
    }

    response = items[item_id]
    return jsonify(response)
