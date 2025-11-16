from rest_framework import serializers

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only=True, many=True)
  categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
      'active',
      'category',
      'categories_id',
    ]

  def create(self, validated_data):
    # 1. Pega os números das categorias e guarda
    category_data = validated_data.pop('categories_id')  # [1, 2]
    
    # 2. Cria o produto SEM as categorias primeiro
    product = Product.objects.create(**validated_data)  # Só title, price, etc.
    
    # 3. Agora adiciona cada categoria ao produto
    for category in category_data:          # Para cada ID (1, 2)
        product.category.add(category)      # Conecta categoria ao produto
    
    # 4. Retorna o produto pronto
    return product