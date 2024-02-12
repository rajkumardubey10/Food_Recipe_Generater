# Food Recipe Generator Using Image 

# Problem Statement:
Create a web app, "Dish Recipe Generator," enabling users to upload dish photos for automatic recipe generation. Challenges include developing an algorithm for automated recipe synthesis, integrating with Gemini Pro APIs, and ensuring a user-friendly interface while maintaining recipe quality and accuracy.

![Python 3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg) ![Gemini Pro](https://img.shields.io/badge/Gemini_Pro-API-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red.svg)

# Software And Tools Requirements

1. [Github Account](https://github.com)
2. [Azure Account](https://azure.microsoft.com/en-us/free)
3. [VS Code IDE](https://code.visualstudio.com)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
## Creat a new environment
```
conda create -p venv python==3.11.4 -y
```
# Demo : 
https://github.com/rajkumardubey10/Food_Recipe_Generater/assets/144990687/e5075b97-b79e-426c-a054-4fcf32279860
# Overview :
The Dish Recipe Generator is a web application built using Streamlit that allows users to upload photos of any dish and generate a recipe using the Gemini Pro APIs. The application leverages the concept of prompt engineering to provide users with detailed recipes based on the visual representation of the dish.
# Scope : 
The scope of the Food Recipe Generator project includes developing a web application that allows users to upload photos of dishes and automatically generate detailed recipes. Key features include automated recipe generation based on visual analysis, integration with external APIs for enhanced functionality, and a user-friendly interface for seamless interaction. The project aims to provide users with accurate and high-quality recipes while offering opportunities for future expansion and refinement.

# Feature :
Upload photos: Users can upload a photo of any dish directly through the web interface.
Generate Recipe: With a single click, users can generate a detailed recipe based on the uploaded photo using Gemini Pro APIs.
Prompt Engineering: The application utilizes prompt engineering techniques to provide comprehensive and easy-to-follow recipes.

# Installation :
### Clone the repository:
```
git clone https://github.com/rajkumardubey10/Food_Recipe_Generater.git
```

### Navigate to the project directory :
```
cd Food_Recipe_Generater
```
### Install the dependencies:
```
pip install -r requirements.txt
```
# Usage :
### Run the Streamlit application :
```
streamlit run app.py
```
Open a web browser and navigate to http://localhost:8501 to access the application.

Upload a photo of a dish and click on the "Generate Recipe" button to receive the recipe.
