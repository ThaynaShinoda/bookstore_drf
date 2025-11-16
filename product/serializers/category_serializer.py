from rest_framework import serializers
from product.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    extra_kwargs = {"slug": {"required": False}}