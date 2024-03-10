#DatbaseOps
''''
This program operates Meal planner user database
Date: 2024.3.9
Author: Alice Lin
'''
import sqlite3
from datetime import datetime
connection = sqlite3.connect("Meal_Planner.db")
cursor = connection.cursor()

# Create User_Profile table
cursor.execute('''
CREATE TABLE IF NOT EXISTS User_Profile (
    UserID INTEGER PRIMARY KEY UNIQUE,
    Username TEXT,
    Age INTEGER,
    Height REAL,
    Weight REAL,
    Dietary_preference TEXT,
    Ingredient_to_avoid TEXT,
    Intolerance TEXT
)
''')
# Commit the changes
connection.commit()
# Sample User
cursor.execute("INSERT INTO User_Profile (UserID, Username, Age, Height, Weight, Dietary_preference, Ingredient_to_avoid, Intolerance) VALUES (00000000, 'John', 25, 175.0, 70.0, 'Vegetarian', 'Peanuts', 'Lactose')")


# Create a unique table for each user
def create_user_Intake(user_id):
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS User_{user_id} (
        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Calories INTEGER,
        Carbs REAL
        FOREIGN KEY (UserID) REFERENCES User_Profile (User ID)
    )
    ''')
    connection.commit()


# Close the connection
connection.close()
