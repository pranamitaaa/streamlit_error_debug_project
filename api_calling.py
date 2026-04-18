import google.generativeai as genai
from dotenv import load_dotenv
import os ,io

#loading the environment variable 
load_dotenv() 

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client 
client = genai.Client(api_key= my_api_key)

def error_explanation(images,selected_option):
    prompt=f"Explain the errors occurs in the {images}."
    response=client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=[images,prompt]
    )

    return response.text

def correct_code(images,selected_option):
    prompt=f"Give the {selected_option} based on the images to fix the error."
    response=client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=[images,prompt]
    )

    return response.text     
