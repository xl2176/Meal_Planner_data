#Meal Planner: Calorie calculator
'''
This is a calorie calculator. It will calculate the calorie from a recipe. and the data will be stored.
API Used: 
    Nutrition API: https://api-ninjas.com/api/nutrition 
Date: 2024.3.9
Author: Alice Lin 
For HackHer
'''
import requests

def get_recipe_info(recipe):
    '''
    This function gets data from the recipe
    param: recipe (a list)
    return: data (a list of dictionary): the data of eac
    '''
    #API Call: https://api-ninjas.com/api/nutrition
    data = []
    for item in recipe:
        query = item
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'srjEtGD5ts7XRyMuzRZvzA==pKa0qlZ6dXSJfOLx'})
        if response.status_code == requests.codes.ok:
            element = response.json()
            data.append(element[0])
        else:
            print("Error:", response.status_code, response.text)
    return data
'''
def get_quality_info():
    
    this function gets quality info from the user
    param: data
    return: quality
    
    quality = float(input("how many grams?"))
    return quality
'''
def update_data(data):
    '''
    this function update the quality data by user input
    param: data
    return: data
    '''
    for item in data:
        print(item["name"])
        quality = float(input("how many grams?"))
        item['serving_size_g'] = quality
    return data

def calculate_calories(data):
    '''
    This function calculates the calories of each recipe
    param: data
    return: Total_cal
    '''
    total_cal = 0
    for item in data:
        total_cal += item.get("calories", 0)
    return total_cal

def calculate_carbohydrates(data):
    '''
    This function calculates the carbohydrates of each recipe
    param: data
    return: total_carb
    '''
    total_carb = 0
    for item in data:
        total_carb += item.get("carbohydrate", 0)
    return total_carb
    
#For testing only
def main():
    '''
    1. Get input 'recipe': which should be a list
    2. put convert into 'query': which specify the quality and name of the material
    3. let it run thru the nutrition API, and gets the 'cal': which is an int
    4. add up the total 'cal' for the recipe return the 'daily_cal' -> store that in a database
    '''
    recipe = ['apple', 'banana', 'orange']
    data = get_recipe_info(recipe)
    data = update_data(data)
    print(data)
    print(calculate_calories(data))
    print(calculate_carbohydrates(data))
    
main()
