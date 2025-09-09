import pytest
from order.models.order import Order
from product.models.product import Product
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create_user(username="usuario_teste", password="senha123")
    product = Product.objects.create(title="Livro Teste", price=30)
    order = Order.objects.create(user=user)
    order.product.add(product)
    assert order.user.username == "usuario_teste"
    assert product in order.product.all()
