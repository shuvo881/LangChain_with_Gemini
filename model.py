import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

class Identifier:
    def __init__(self, name):
        self.name = name
        genai.configure(api_key=os.environ["API_KEY"])

    def get(self):
        return genai.GenerativeModel(self.name)
        


