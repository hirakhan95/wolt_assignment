from delivery_fee_calculator.utils import calculate_delivery_fee


# cart_value is 200€
def test_free_delivery():
    assert calculate_delivery_fee(20000, 1000, 3, "2024-01-20T15:00:00Z") == 0
    assert calculate_delivery_fee(23000, 1000, 3, "2024-01-20T15:00:00Z") == 0


# cart_value less than 10 €
def test_small_order():
    assert calculate_delivery_fee(500, 1000, 3, "2024-01-20T15:00:00Z") == 700


# cart_value is more than 10€
def test_large_order():
    assert calculate_delivery_fee(1500, 1000, 3, "2024-01-20T15:00:00Z") == 200


# delivery_distance when 1000 meters
def test_delivery_distance_fee():
    assert calculate_delivery_fee(1500, 1000, 3, "2024-01-20T15:00:00Z") == 200


# delivery_distance greater than 1000 meters
def test_additional_distance_fee():
    assert calculate_delivery_fee(1000, 2499, 3, "2024-01-20T15:00:00Z") == 500


# number_of_items more than 12 items
def test_bulk_item_fee():
    assert calculate_delivery_fee(1500, 1000, 15, "2024-01-20T15:00:00Z") == 869


# order during friday rush hours
def test_friday_rush_hour():
    assert calculate_delivery_fee(1500, 1000, 3, "2024-01-26T16:00:00Z") == 240
    assert calculate_delivery_fee(1500, 1000, 3, "2024-01-26T15:20:00Z") == 240
    assert calculate_delivery_fee(1500, 1000, 3, "2024-01-26T18:59:00Z") == 240


# order during friday (not rush hours)
def test_friday_not_so_rush_hour():
    assert calculate_delivery_fee(1500, 1000, 3, "2024-01-26T10:00:00Z") == 200
    assert calculate_delivery_fee(1500, 1000, 7, "2024-01-26T13:00:00Z") == 350


# maximum delivery_fee
def test_maximum_delivery_fee():
    assert calculate_delivery_fee(500, 5000, 15, "2024-01-26T10:00:00Z") == 1500
