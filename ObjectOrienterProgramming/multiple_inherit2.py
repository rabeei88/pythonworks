
class Cusine:
    cusine_name=str

    def __init__(self,cusine_name):
        self.cusine_name=cusine_name

    def dispaly_cusine_info(self):
        print(self.cusine_name)


class MealType:
    mealtype=str

    def __init__(self,mealtype):
        self.mealtype=mealtype

    def display_meal_info(self):
        print(self.mealtype)


class Dish(Cusine,MealType):
    dish_name=str

    def __init__(self,cusine_name,mealtype,dish_name):
        Cusine.__init__(self,cusine_name)
        MealType.__init__(self,mealtype)
        self.dish_name=dish_name

    def display_dish_info(self):

        self.dispaly_cusine_info()
        self.display_meal_info()

        print(self.dish_name)

dish_instance=Dish("ITALIAN","BREAKFAST","ITALIAN PASTA")
dish_instance.display_dish_info()



    



