from models.dish import Dish
import csv
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.list_of_dishes = {}

        with open(source_path, "r", encoding="utf-8") as file:
            _header, *datas = csv.reader(file, delimiter=',')
        self.dishes.update(self.get_list_dishes(datas))

    def get_list_dishes(self, datas):
        for dish, price, ingredient, recipe_amount in datas:
            if dish not in self.list_of_dishes:
                self.list_of_dishes[dish] = Dish(
                    dish, float(price))
            ingredient = Ingredient(ingredient)
            self.list_of_dishes[dish].add_ingredient_dependency(
                    ingredient, int(recipe_amount)
                )
        return self.list_of_dishes.values()
