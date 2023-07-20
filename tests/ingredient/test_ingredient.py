from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # https://www.pythontutorial.net/python-oop/python-__eq__/
    assert Ingredient("ovo").__eq__(Ingredient("ovo"))

    # https://www.pythontutorial.net/python-oop/python-__hash__/
    assert Ingredient("ovo").__hash__() == hash("ovo")

    assert Ingredient("ovo").name == "ovo"

    # https://www.pythontutorial.net/python-oop/python-__repr__/
    assert Ingredient("ovo").__repr__() == "Ingredient('ovo')"

    assert Ingredient("ovo").restrictions == {Restriction.ANIMAL_DERIVED}
