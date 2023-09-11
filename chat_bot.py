import openai
from api_key import open_ai_api_key

openai.api_key = open_ai_api_key

def get_response(message) :
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages = message )
    return response['choices'][0]['message']
    