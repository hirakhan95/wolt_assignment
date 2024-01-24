from datetime import datetime, timezone
import math
from dateutil import parser

"""
Rules for calculating delivery fee
"""


def calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time):

    cart_value_eur = cart_value / 100.0
    delivery_fee = 0.0

    # Delivery fee will be calculated only if cart_value is less than 200 € else shipping will be free of cost
    if cart_value_eur < 200:

        # Delivery fee according to cart value
        if cart_value_eur < 10:
            surcharge = 10 - cart_value_eur
            delivery_fee = delivery_fee + round(surcharge, 2)

        # Delivery fee according to distance
        delivery_fee += 2
        if delivery_distance > 1000:
            additional_distance = delivery_distance - 1000
            additional_fee = math.ceil(additional_distance / 500)
            delivery_fee += additional_fee

        # Delivery fee according to number of items in a cart
        if number_of_items >= 5:
            delivery_fee += (number_of_items - 4) * 0.50
        if number_of_items > 12:
            delivery_fee += 1.20

        # Delivery fee according to friday rush hours
        dt_obj = parser.parse(time)

        if dt_obj.isoweekday() == 5:
            if dt_obj.hour in [15,16,17,18]:
                delivery_fee *= 1.2

        # Delivery fee should not be more than 15 €
        delivery_fee = min(delivery_fee, 15)

    return int(delivery_fee * 100)