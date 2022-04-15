from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','title','body','product','product_id']
        depth = 1

    product_id = serializers.IntegerField(write_only=True)
