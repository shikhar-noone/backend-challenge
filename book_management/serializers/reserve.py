from rest_framework import serializers
from book_management.models.reserve import ReservedProduct

class ReserveBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReservedProduct
        fields = "__all__"
