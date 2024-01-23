from django.urls import path
from delivery_fee_calculator.views import DeliveryFeeView


urlpatterns = [
    path('', DeliveryFeeView.as_view(), name='calculate_fee'),
]
