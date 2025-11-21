import pytest
from product.models.product import Product
from product.models.category import Category

@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(title="Romance", slug="romance")
    product = Product.objects.create(
        title="Livro Teste",
        description="Descrição do livro",
        price=50,
        active=True
    )
    product.categorie.add(category)
    assert product.title == "Livro Teste"
    assert product.description == "Descrição do livro"
    assert product.price == 50
    assert product.active is True
    assert category in product.categorie.all()
