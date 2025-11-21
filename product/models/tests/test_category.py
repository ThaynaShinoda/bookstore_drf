import pytest
from product.models.category import Category

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title="Ficção",
        slug="ficcao",
        description="Livros de ficção",
        active=True
    )
    assert category.title == "Ficção"
    assert category.slug == "ficcao"
    assert category.description == "Livros de ficção"
    assert category.active is True
