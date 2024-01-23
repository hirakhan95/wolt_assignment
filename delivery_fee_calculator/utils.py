from datetime import datetime, timezone
import math

"""
Rules for calculating delivery fee
"""


def calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time):

    cart_value_eur = cart_value / 100.0
    delivery_fee = 0.0

    # 1. Delivery fee according to cart value
    if cart_value_eur < 10:
        surcharge = 10 - cart_value_eur
    delivery_fee = delivery_fee + round(surcharge, 2)

    # 2. Delivery fee according to distance
    if delivery_distance > 1000:
        delivery_fee += 2

        additional_distance = delivery_distance - 1000
        additional_fee = additional_distance / 500
        delivery_fee += math.ceil(additional_fee)

    else:
        delivery_fee += 2

    # 3. Delivery fee according to number of items in a cart
    surcharge = 0
    for item in range(1, number_of_items + 1):
        if item >= 5:
            surcharge = (item - 4) * 0.50
            if item > 12:
                surcharge += 1.20

    # 4. Delivery fee if cart_value exceeds 200 €
    delivery_fee = min(delivery_fee, 15)

    # 5. Delivery fee if cart_value exceeds 200 €
    if cart_value >= 200:
        delivery_fee = 0

    # 6. Delivery fee according to time

    # d = datetime.fromisoformat(time).astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    # dt_obj = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    #
    # if dt_obj.isoweekday() == 5:
    #     if dt_obj.hour == 15 or dt_obj.hour == 16 or dt_obj.hour == 17 or dt_obj.hour == 18 or dt_obj.hour == 19:
    #         delivery_fee *= 1.2

    return int(delivery_fee * 100)