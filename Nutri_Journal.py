
from Nutri import Nutrition, Breakfast, Lunch, Dinner



def main():
    
    print("****WELCOME TO NUTRI-DIARIES!****")

    fname = "all_nutritionfacts.csv"
    lst_nutrients = []

    lst_nutrients = load_nutrients(fname)


    while(True): 
        nutrition = insert_nutrition()
        if nutrition == None:
            break

        lst_nutrients.append(nutrition)
    
    print("\n\n*****Nutrional Logs*****")
    for elem in lst_nutrients:
        print(elem)

    save_nutrients(fname, lst_nutrients)
    print("\n\n")


def save_nutrients(fname, lst_nutrients):
    with open(fname, "w") as f:
        for nutrition in lst_nutrients:
            if type(nutrition) == Breakfast:
                f.write("Breakfast:, " + nutrition._food_item + ", CAL: " + str(nutrition._calorie) + ", FAT: " + str(nutrition._fat)  + ",  CARB: " + str(nutrition._carb) + ", PROT: " + str(nutrition._protein) + ", SODI: " + str(nutrition._sodium) + ", SUGAR: " + str(nutrition._sugars))

            elif type(nutrition) == Lunch:
                f.write("Lunch:, " + nutrition._food_item + ", CAL: " + str(nutrition._calorie) + ", FAT: " + str(nutrition._fat)  + ",  CARB: " + str(nutrition._carb) + ", PROT: " + str(nutrition._protein) + ", SODI: " + str(nutrition._sodium) + ", SUGAR: " + str(nutrition._sugars))
            
            elif type(nutrition) == Dinner:
                f.write("Dinner:, " + nutrition._food_item + ", CAL: " + str(nutrition._calorie) + ", FAT: " + str(nutrition._fat)  + ",  CARB: " + str(nutrition._carb) + ", PROT: " + str(nutrition._protein) + ", SODI: " + str(nutrition._sodium) + ", SUGAR: " + str(nutrition._sugars))
            else: 
                pass

def load_nutrients(fname):
    lst_nutrients = []

    with open(fname, "r") as f:
        for line in f:
            info = line.split(',')
            if info[0] == "Breakfast":
                nutrition = Breakfast(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
            elif info[0] == "Lunch":
                nutrition = Lunch(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
            elif info[0] == "Dinner":
                nutrition = Dinner(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
            else:
                nutrition = None

            if nutrition != None:
                lst_nutrients.append(nutrition)
    return lst_nutrients

def insert_nutrition() -> Nutrition:
    print("\nPlease select which meal we will be logging today!")
    print("\t1) Breakfast")
    print("\t2) Lunch")
    print("\t3) Dinner")
    print("\t4) quit")
    meal_type = input(">>> ")



    #if meal_type == "4":
        #return 
    if meal_type not in ["1", "2", "3",]:
            return None

   
      
           
    food_item = str(input("\nEnter Food item: \n>>>"))
    calorie = int(input("\nEnter Calories: \n>>>"))
    fat = int(input("\nEnter Fat Content: \n>>>"))
    carb = int(input("\nEnter Carbohydrates: \n>>>"))
    protein = int(input("\nEnter Protein: \n>>>"))
    sodium = int(input("\nEnter Sodium: \n>>>"))
    sugars = int(input("\nEnter Sugars: \n>>>"))
    
    
   
    
    if meal_type == "1":
        nutrition = Breakfast(food_item, calorie, fat, carb, protein, sodium, sugars)
    elif meal_type == "2":
         nutrition = Lunch(food_item, calorie, fat, carb, protein, sodium, sugars)
    elif meal_type == "3":
         nutrition = Dinner(food_item, calorie, fat, carb, protein, sodium, sugars)
    else: 
        nutrition = None

    return nutrition

if __name__ == "__main__":
    main()