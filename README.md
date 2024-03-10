## Welcome to NutroVision: Your Insightful Guide to Nutritious Eating 

_In this repository, we didn't endup using any of the codes form the Meal_panner_databse.py, User_data_input.py, DatbaseOps.py, and file_
Discover Recipes, Uncover Nutrients, and Track Calories Seamlessly

Transform Your Ingredients into Nutritional Insights NutroVision is revolutionizing the way you cook and track your nutrition. With our innovative app, you can turn a simple image of ingredients into a detailed culinary adventure, complete with calorie counts and nutritious recipes.

### How NutroVision Works
#### Capture or Upload Your Ingredients
- Take a photo of your kitchen ingredients or upload an image from your gallery to get started. Smart Ingredient Recognition
- Utilizing cutting-edge image recognition technology, NutroVision identifies your ingredients and lists them neatly for you.
#### Explore Customized Recipe Suggestions
- Based on the identified ingredients, NutroVision offers a variety of recipes tailored to your pantry, helping you whip up delicious meals effortlessly.
#### Nutritional Insight and Calorie Tracking
- Choose any recipe to see a comprehensive bar chart of its calorie content, helping you maintain a balanced diet with every meal.

### Key Features
- ntuitive Ingredient-to-Recipe Conversion
- Make the most of your ingredients with personalized recipe recommendations.
- Detailed Caloric Breakdown
- Understand the nutritional content of your meals with easy-to-read bar charts.
- Seamless User Experience
- Enjoy cooking with a user-friendly interface designed for food lovers and health-conscious individuals alike.
- Why NutroVision?
- NutroVision is more than just a recipe app; it's your personal nutritionist in your pocket, empowering you to make healthier food choices based on the ingredients you have at hand.

### Ready to Dive into a World of Nutritional Clarity?
Download NutroVision now and start transforming your ingredients into healthy, delicious meals while keeping track of your dietary goals!

### In Nutro Vision, We use Image recognition technique base on CNN model
This project focuses on creating a convolutional neural network (CNN) model to classify images of fruits and vegetables. Utilizing TensorFlow and Keras, the model aims to accurately identify various types of produce from a dataset, highlighting the power of deep learning in image recognition tasks.

#### Dataset Preparation
The dataset, stored on Google Drive, comprises images of 36 different classes of fruits and vegetables. It's divided into training, validation, and test sets with 3145, 351, and 359 images, respectively. TensorFlow's image_dataset_from_directory method is used to load these images and prepare them for the model.

#### Model Architecture
The CNN model architecture includes:

*Input Layer*: Accepts images with dimensions 64x64 pixels in RGB color mode. 
*Convolutional Layers*: Two sets of convolutional layers with ReLU activation. The first set has 32 filters, and the second set has 64 filters, both with a kernel size of 3x3. 
*Max Pooling Layers*: Follow each convolutional layer set to reduce spatial dimensions. 
*Dropout Layers*: Included after max pooling layers to prevent overfitting by randomly dropping 25% of the units. 
*Flatten Layer*: Converts the 2D matrix data to a vector that can be fed into the dense layers. Dense Layers: Two fully connected layers with 512 and 256 units, respectively, using ReLU activation. 
*Output Layer*: A dense layer with 36 units (one for each class) and softmax activation to output classification probabilities.

#### Training the Model
The model is compiled with the Adam optimizer and categorical cross entropy as the loss function, suitable for multi-class classification. Training is performed over 32 epochs, showing gradual improvement in accuracy and loss reduction on both training and validation datasets.

#### Results and Evaluation
The model achieved high accuracy, with 88.36% on the training set and 86.30% on the validation set, indicating strong learning and generalization. However, it’s essential to monitor for overfitting, despite regularization efforts like dropout layers. The test set accuracy further validated the model's effectiveness, showing a 96.38% accuracy rate.
