from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DeliveryFeeSerializer
from .utils import calculate_delivery_fee


class DeliveryFeeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DeliveryFeeSerializer(data=request.data)
        if serializer.is_valid():
            fee = calculate_delivery_fee(
                serializer.validated_data['cart_value'],
                serializer.validated_data['delivery_distance'],
                serializer.validated_data['number_of_items'],
                serializer.validated_data['time']
            )
            return Response({'delivery_fee': fee})
        return Response(serializer.errors, status=400)
