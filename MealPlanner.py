import requests
import json
import streamlit as st
import tensorflow as tf
import numpy as np

apiKey = "7d7e21ebac264d65910cd1dd2819f35b"

with open("prediction_result.txt", "w") as file:
    pass

def jsonToEnlgish(analyzed, recipe):
    st.write(recipe["title"])
    st.image(recipe["image"])
    st.write("Source: ", recipe["sourceUrl"])
    st.write("Ingredient List")
    for i in range(0,len(recipe["extendedIngredients"])):
        st.markdown("- " + recipe["extendedIngredients"][i]["original"])
        
    for i in range(0,len(analyzed)):
        for x in range(0, len(analyzed[i]["steps"])):
            st.subheader("Step " + str(analyzed[i]["steps"][x]["number"]) + ": ")
            st.write(analyzed[i]["steps"][x]["step"])
            
def model_prediction(test_image):
    model = tf.keras.models.load_model("finalfile.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)
            
dietaryPreference = ""
ingredientsToAvoid = ""
intolerances = ""
username = ""
userID = "XXXX0000"
age = -1
height = -1
weight = -1


#streamlit run C:\Users\David\MealPlanner.py
homepage, profile, search, recommendations, imageRec= st.tabs([":house: Home", ":person_in_tuxedo: Profile",":mag: Search Recipes", ":thumbsup: Recommendations", ":camera: Inventory and Upload"])

with homepage:
    st.header("Welcome to NutroVision: Your Insightful Guide to Nutritious Eating")
    st.image("Home1.png")

    percentage_value = 9

    with st.expander('', expanded=True):
        st.markdown(f'''
        ##### Transform Your Ingredients into Nutritional Insights
        <ul style="padding-left:20px">
        <li>NutroVision is revolutionizing the way you cook and track your nutrition. With our innovative app, you can turn a simple image of ingredients into a detailed culinary adventure, complete with calorie counts and nutritious recipes.</li>
        </ul>
        ''', unsafe_allow_html=True)

    with st.expander('', expanded=True):
        st.markdown(f'''
        ##### How NutroVision Works: 
        <ul style="padding-left:20px">
        <li>Capture or Upload Your Ingredients
            <ul><li>Take a photo of your kitchen ingredients or upload an image from your gallery to get started.</li></ul>
        </li>
        
        <li>Smart Ingredient Recognition
            <ul><li>Utilizing cutting-edge image recognition technology, NutroVision identifies your ingredients and lists them neatly for you.</li></ul>
        </li>
        
        <li>Explore Customized Recipe Suggestions
            <ul><li>Based on the identified ingredients, NutroVision offers a variety of recipes tailored to your pantry, helping you whip up delicious meals effortlessly.</li></ul>
        </li>
                    
        <li>Nutritional Insight and Calorie Tracking
            <ul><li>Choose any recipe to see a comprehensive bar chart of its calorie content, helping you maintain a balanced diet with every meal.</li></ul>
        </li>            
        </ul>
        ''', unsafe_allow_html=True)

with profile:
    pass
    st.write("User ID: ", userID)
    username = st.text_input("Username")
    age = int(st.slider("Age",min_value=0,max_value=140))
    height = st.text_input("Height",value = 0)
    weight = st.text_input("Weight", value = 0)
    sex = st.selectbox("Biological Sex",["Male","Female"])
    dietaryPreference = st.selectbox("Diet", ["", "Gluten Free", "Ketogenic", "Vegetarian", "Lacto-Vegetarian", "Ovo-Vegetarian", "Vegan", "Pescetarian", "Paleo", "Primal","Low FODMAP", "Whole30"])
    ingrdientsToAvoid = st.text_area("Ingridents to Avoid")
    intolerances = st.text_area("Food Intolerances")
      
with search:
    with st.expander("Filter"):
        includeCuisines = st.multiselect("Cuisines", ["","African","Asian","American","British","Cajun","Caribbean","Chinese","Eastern European","French","German","Greek","Indian","Irish","Italian","Japanese","Jewish","Korean","Latin American","Mediterranean","Mexican","Middle Eastern","Nordic","Southern","Spanish","Thai","Vietnamese"])
        excludeCusines = st.multiselect("Exclude Cuisines", ["","African","Asian","American","British","Cajun","Caribbean","Chinese","Eastern European","French","German","Greek","Indian","Irish","Italian","Japanese","Jewish","Korean","Latin American","Mediterranean","Mexican","Middle Eastern","Nordic","Southern","Spanish","Thai","Vietnamese"])
        maxReadyTime = st.slider("Ready Time (Minutes)", min_value = 0, max_value = 300, value = 300)
    
        minCal = st.text_input("Minimum Calories (Grams)", value = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age)))
        maxCal = st.text_input("Maximum Calories (Grams)", value = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age)))
        
        minCarb = st.text_input("Minimum Carbohydrates (Grams)",value = 0)
        maxCarb = st.text_input("Maximum Carbohydrates (Grams)", value = 300)
        
        minFat = st.text_input("Minimum Fats (Grams)", value = 0)
        maxFat = st.text_input("Maxiumum Fats (Grams)", value = 300)
        
        minPro = st.text_input("Minimum Proteins (Grams)", value = 0)
        maxPro = st.text_input("Maximum Proteins (Grams)", value = 300)
        
    search = st.text_input("Search:")
    
    if (minCal == "" and sex == "Male" and height != "" and weight != ""):
        minCal = 88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (5.677 * age)
        minCal = minCal//3
    elif (minCal == "" and sex == "Female" and height != "" and weight != ""):
        minCal = 447.593 + (9.247 * int(weight)) + (3.098 * int(height)) - (4.330 * age)
        minCal = minCal//3
    
    with open("prediction_result.txt", "r") as file:
        inventory = file.read()

    parameters = {
        "query":search,
        "cuisine": includeCuisines,
        "excludeCuisine": excludeCusines,
        "diet": dietaryPreference,
        "intolerances":intolerances,
        "includeIngredients":inventory,
        "excluedeIngredients": ingredientsToAvoid,
        "instructionsRequired":True,
        "maxReadyTime": maxReadyTime,
        "minCarbs":minCarb,
        "maxCarbs":maxCarb,
        "minProtein":minPro,
        "maxProtein":maxPro,
        "minCalories":minCal,
        "maxCalories":maxCal,
        "minFat":minFat,
        "maxFat":maxFat
    }
    
    if search != "":
        response = requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=" + apiKey, params = parameters)
        
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        data = json.loads(text)
        
        ids = {}
    
        for i in range(0,len(data["results"])):
            ids[data["results"][i]["title"]] = data["results"][i]["id"]

        select = st.selectbox("Choose a recipe", ids.keys())
        
        response = requests.get("https://api.spoonacular.com/recipes/" + str(ids[select]) + "/analyzedInstructions?apiKey=" + apiKey)
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        analyzed = json.loads(text)
        
        response = requests.get("https://api.spoonacular.com/recipes/" + str(ids[select]) + "/information?apiKey=" + apiKey)
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        recipe = json.loads(text)
        
        jsonToEnlgish(analyzed, recipe)

with open("prediction_result.txt", "r") as file:
    inventory = file.read()
        
with recommendations:
    parameters = {
        "cuisine": includeCuisines,
        "excludeCuisine": excludeCusines,
        "diet": dietaryPreference,
        "intolerances":intolerances,
        "includeIngredients":inventory,
        "excluedeIngredients": ingredientsToAvoid,
        "instructionsRequired":True,
        "maxReadyTime": maxReadyTime,
        "minCarbs":minCarb,
        "maxCarbs":maxCarb,
        "minProtein":minPro,
        "maxProtein":maxPro,
        "minCalories":minCal,
        "minFat":minFat,
        "maxFat":maxFat
    }

    response = requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=" + apiKey, params = parameters)
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    data = json.loads(text)
    
    ids = {}

    for i in range(0,len(data["results"])):
        ids[data["results"][i]["title"]] = data["results"][i]["id"]

    select = st.selectbox("Choose a recipe", ids.keys())
    
    response = requests.get("https://api.spoonacular.com/recipes/" + str(ids[select]) + "/analyzedInstructions?apiKey=" + apiKey)
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    analyzed = json.loads(text)
    
    response = requests.get("https://api.spoonacular.com/recipes/" + str(ids[select]) + "/information?apiKey=" + apiKey)
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    recipe = json.loads(text)
    
    jsonToEnlgish(analyzed, recipe)

with imageRec:
    st.header("Ingredients")
    test_image=st.file_uploader("Please upload you imgae")

    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)

    if(st.button("Predict")):
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        with open("labels.txt") as f:
            content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
        st.success("Model is Predicting it's a {}".format(label[result_index]))
        
        predicted_label = label[result_index]
        with open("prediction_result.txt", "w") as file:
            file.write(predicted_label + ",")