from rest_framework import serializers


class DeliveryFeeSerializer(serializers.Serializer):
    cart_value = serializers.IntegerField()
    delivery_distance = serializers.IntegerField()
    number_of_items = serializers.IntegerField()
    time = serializers.CharField()
