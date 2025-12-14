import os
from dotenv import load_dotenv
from google import genai
import json
from google.genai import types
from helpers.logger import log


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    client = genai.Client(api_key=api_key) #client initialisation
else:
    print("API key not found in the environment")
    log.error("API key not found in the environment")

def generate_user_data(role_description):
    #determining json schema, fields are equal to User object fields
    json_schema = {
        "type":'object',
        'properties':
            {"name": {'type':"string"},
                "second_name": {"type":"string"},
                "teuda": {"type":"string", "description":"Teuda is 9-digit string"},
                "email": {"type":"string", "format":"email"},
                "phone": {"type":"string", "description":"phone number must use a standard Israeli number format as a string and starts with 055 or 053, "
                                                         "for example: 0559561388"},
                "birth_date":{"type":"string", "format":"date"},
                "aliah_date":{"type":"string",  "description":"Aliah date must contain only 4-digits string (e.g. 2018)"},
                "password": {"type":"string"}
            },
        "required": ["name", "second_name", "teuda", "email", "phone", "birth_date", "aliah_date", "password"]
    }
    #forming a prompt for data generation
    prompt = f"Generate realistic test data for a new user who is '{role_description}'"


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema=json_schema
            )
        )
    data_dict = json.loads(response.text)
    return data_dict



