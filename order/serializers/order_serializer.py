from rest_framework import serializers

from product.models.product import Product
from order.models import Order
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
  product = ProductSerializer(read_only=True, many=True) # Para MOSTRAR
  products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many = True)  # Para RECEBER
  total = serializers.SerializerMethodField()

  def get_total(self, instance):
    total = sum([product.price for product in instance.product.all()])
    return total

  class Meta:
    model = Order
    fields = ['product', 'total', 'user', 'products_id']
    extra_kwargs = {'product': {'required': False}}
  
  def create(self, validated_data):
    # 1. Pega os produtos e o usuário
    product_data = validated_data.pop('products_id')  # [1, 2, 3]
    user_data = validated_data.pop('user')           # 1
    
    # 2. Cria o pedido vazio primeiro
    order = Order.objects.create(user=user_data)
    
    # 3. Adiciona cada produto ao pedido
    for product in product_data:
        order.product.add(product)
    
    return order