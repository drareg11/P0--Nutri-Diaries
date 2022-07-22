#> Data should be read and written to CSV(comma, seperated, vales) or JSON files

#> Command Line Interface where users can interact with the application while its running
#> Application should read in data from a file and be displayed in some way
#> Application should write data to a file
#All user input should be validated (program should not end with exceptions based on user input)
#Program must follow OOP design (classes/objects)
#Application should be uploaded to a GitHub repo.


#Personal Obj
#Nutri journal app to record/track nutrional information
#Records food item and nutrients info
#Nutrients = calories, fat, vit, carbs, proteins, sodium, sugar
#records nutrients and food name in file
#messages can exclaim when proceeding over daily limit

from abc import ABC 

class Nutrition(ABC):
    def __init__(self, food_item, calorie, fat, carb, protein, sodium, sugars=""):
        self._food_item = str(food_item)
        self._calorie = int(calorie)
        self._fat = int(fat)
        self._carb = int(carb)
        self._protein = int(protein)
        self._sodium = int(sodium)
        self._sugars = int(sugars)

    def setName(self, food_item):
        self.food_item = str(food_item)
    
    def getName(self):
        return self.food_item

    def __str__(self): #overriding string default
        return  "FOOD ITEM:" + self._food_item + ", Calories: " + str(self._calorie) + ", Fats: " + str(self._fat) + ", Carbs: " + str(self._carb) + ", Protein: " + str(self._protein) + ", Sodium: " + str(self._sodium) + ", Sugars: " + str(self._sugars)


class Breakfast(Nutrition):
    print()

class Lunch(Nutrition):
    print()
class Dinner(Nutrition): 
    print()
