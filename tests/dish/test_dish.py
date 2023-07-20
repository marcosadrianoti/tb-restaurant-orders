import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    lasanha = Dish('Lasanha', 25.90)
    assert lasanha.name == 'Lasanha'

    assert lasanha.__eq__(lasanha)
    assert lasanha.__hash__() == hash(lasanha)
    assert lasanha.__hash__() != hash(Dish('Lasanha 4 queijos', 30.00))
    assert lasanha.__repr__() == "Dish('Lasanha', R$25.90)"

    ingredient = Ingredient("queijo mussarela")
    lasanha.add_ingredient_dependency(ingredient, 15)
    assert lasanha.recipe == {ingredient: 15}
    assert lasanha.get_ingredients() == {ingredient}

    assert lasanha.get_restrictions() == {Restriction.LACTOSE,
                                          Restriction.ANIMAL_DERIVED}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Lasanha", "25.90")

    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Lasanha", -25.90)
