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
    return: cal_data (a list of dictionary): the data of eac
    '''
    #API Call: https://api-ninjas.com/api/nutrition
    query = get_recipe_info(recipe)
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'srjEtGD5ts7XRyMuzRZvzA==pKa0qlZ6dXSJfOLx'})
    cal_data = []
    if response.status_code == requests.codes.ok:
        for item in recipe:
            item = response.text
            cal_data.append(item)
        return cal_data
    else:
        print("Error:", response.status_code, response.text)



def calculate_calories(recipe):
    '''
    This function calculates the calories of each recipe
    param: recipe
    return cal
    '''
    total_calories = 0
    for food in recipe:
        for item in recipe:
            if item["name"] == food:
                total_calories += item["calories"]
                break
    return cal

def main():
    '''
    1. Get input 'recipe': which should be a list
    2. put convert into 'query': which specify the quality and name of the material
    3. let it run thru the nutrition API, and gets the 'cal': which is an int
    4. add up the total 'cal' for the recipe return the 'daily_cal' -> store that in a database
    '''
