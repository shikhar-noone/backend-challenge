from rest_framework import serializers
from book_management.models.checkout import CheckoutProduct

class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckoutProduct
        fields = "__all__"
