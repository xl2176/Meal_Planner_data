#Database_operation
import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",      # Replace with your MySQL host
    user="your_username",  # Replace with your MySQL username
    password="your_password",  # Replace with your MySQL password
    database="Meal_Planner"  # Replace with your database name
)

# Create cursor
mycursor = mydb.cursor()

# Function to create User_Profile table
def create_user_profile_table():
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS User_Profile (
            username VARCHAR(50),
            userID INT(8) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            age INT,
            height FLOAT,
            weight FLOAT,
            dietary_preference VARCHAR(255),
            ingredient_to_avoid VARCHAR(255),
            intolerance VARCHAR(255)
        )
    """)

# Function to create user intake table
def create_user_intake_table(userID):
    # Define table name
    table_name = f"user_{userID}"

    # Create table for user intake
    mycursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            date DATE,
            intake_calories FLOAT,
            intake_carbohydrate FLOAT,
            PRIMARY KEY (date)
        )
    """)


# Create User_Profile table
create_user_profile_table()

# Create user intake tables for each user
for userID in userIDs:
    create_user_intake_table(userID)

# Commit changes and close connection
mydb.commit()
mydb.close()
