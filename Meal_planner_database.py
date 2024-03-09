#Meal Planner: Calorie data base
'''
This file connect to a SQL database: "Meal_Planner"
date: 2024.3.9
Author: Alice Lin
For HackHer
'''
import mysql.connector
from Calorie_calculator import get_recipe_info, update_data, calculate_calories, calculate_carbohydrates
import hashlib
import time
from datetime import datetime

mydb = mysql.connector.connect
(
    host = 'P_XINYAOLIN-MB0'
    user = 'root'
    password = '030507ABc!'
    database = 'Meal_Planner'
)
    

def id():
    # Generate a unique ID based on current timestamp and a random number
    unique_id = str(time.time()) + str(hashlib.sha256(str(time.time()).encode()).hexdigest())[:4]
    # Take the last 8 digits
    unique_id = unique_id.replace('.', '')[-8:]
    return id

def date():
    # Get the current date
    current_date = datetime.now().date()
    # Format the date as a string
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date

def add_use():
    '''
    This create a user to the database
    '''
    # Create cursor
    mycursor = mydb.cursor()
    # Define variables
    UserID = id
    Username = input("Please enter your username (under 50 words):")
    Age = int(input("Please enter your age"))
    Height = int(input("Please enter your height (in cm)"))
    Weight = int(input("Please enter your weight (in kg)"))
    Dietary_preference = input("Please enter your dietary preference (vegetarian, vegan, etc.)")
    Ingredient_to_avoid = input("Please enter ingredient to avoid:")
    Intolerance = input("Please enter intolerance:")
    sql = "UPDATE user_profile SET Username = %s, Age = %s, Height = %s, Weight = %s, Dietary_preference = %s, Ingredient_to_avoid = %s, Intolerance = %s WHERE UserID = %s"
    values = (Username, Age, Height, Weight, Dietary_preference, Ingredient_to_avoid, Intolerance, UserID)
    mycursor.execute(sql,values)
    mydb.commit()
    mydb.close()

def add_intake():
    '''
    this create an daily intake for a user.
    '''
# Update user intake table
sql = "UPDATE daily_intake SET total_calories = %s, total_carbs = %s WHERE userID = %s AND date = %s"
values = (calories, carbs, userID, date)

mycursor.execute(sql, values)


# Commit changes to the database
mydb.commit()

# Close the connection
mydb.close()






