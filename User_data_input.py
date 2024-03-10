#User_data_input
'''
This program will ask user input and store in the database
Date: 2024.3.9
Author: Alice Lin
'''
import sqlite3
import hashlib
import time
from Calorie_calculator import calculate_carbohydrates, calculate_calories, update_data
#Generate Unique ID
def id():
    # Generate a unique ID based on current timestamp and a random number
    unique_id = str(time.time()) + str(hashlib.sha256(str(time.time()).encode()).hexdigest())[:4]
    # Take the last 8 digits
    unique_id = unique_id.replace('.', '')[-8:]
    return id

connect = sqlite3.connect('Meal_Planner.db')
cursor = connect.cursor()
#add a user to User_Profile
def add_user():
    """Ask the user for input and add a new user to the User_Profile table."""
    username = input("Enter username: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height (cm): "))
    weight = float(input("Enter weight (kg): "))
    dietary_preference = input("Enter dietary preference: ")
    ingredient_to_avoid = input("Enter ingredient to avoid: ")
    intolerance = input("Enter intolerance: ")
    user_id = id()
    cursor.execute("INSERT INTO User_Profile (UserID, Username, Age, Height, Weight, Dietary_preference, Ingredient_to_avoid, Intolerance) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (user_id, username, age, height, weight, dietary_preference, ingredient_to_avoid, intolerance))
    connect.commit()
    print(f"User added successfully! Your UserID is: {user_id}")

def add_intake(user_id, data):
    """Ask the user for input and add a new intake to the User_{user_id} table."""
    data = update_data
    calories = calculate_calories(data)
    carbs = calculate_carbohydrates(data)
    cursor.execute(f"INSERT INTO User_{user_id} (Calories, Carbs) VALUES (?, ?)", (calories, carbs))
    connect.commit()

    print(f"Intake added successfully for UserID: {user_id}")

# Example usage: add a new user and add an intake for the user
user_id = add_user()
add_intake(user_id)

# Close the connection
connect.close()


