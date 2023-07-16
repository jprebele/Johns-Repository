# John Rebeles
# PSID: 2039426
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0, num_servings=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.num_servings = num_servings

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(self.num_servings,
                                                                        self.get_calories(self.num_servings)))


if __name__ == "__main__":
    user_name = input()
    user_fat = float(input())
    user_carbs = float(input())
    user_protein = float(input())
    user_servings = float(input())

    food = FoodItem('None', 0, 0, 0, user_servings)
    food.print_info()

    print()
    food = FoodItem(user_name, user_fat, user_carbs, user_protein, user_servings)
    food.print_info()
