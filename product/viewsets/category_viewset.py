from rest_framework.viewsets import ModelViewSet
from product.models import Category
from product.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet) :
  serializer_class = CategorySerializer

  #Essa é uma outra maneira de declarar o queryset
  def get_queryset(self):
    return Category.objects.all()