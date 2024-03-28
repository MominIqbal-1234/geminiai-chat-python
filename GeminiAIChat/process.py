import os
import httpx
import requests
from dotenv import load_dotenv
import json
load_dotenv()
import google.generativeai as genai


class GET:
    def __init__(self,api):
        self.KEY =  api
        self.API_URL =  f"{os.environ.get('API_URL') + self.KEY}"
        self.PROMPT =  f"{os.environ.get('PROMPT')}"
        self.PROMPT = json.loads(self.PROMPT)

        
    def sendResponse(self,prompt):
        self.prompt = prompt
        
    def retrieveShortResponse(self):
        try:
            self.PROMPT['contents'][0]['parts'][0]['text'] = self.prompt
            self.response = requests.post(
                self.API_URL,
                headers={'Content-Type': 'application/json'},
                json=self.PROMPT).json()
            return self.response['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            raise ValueError({"message":e})

    def retrieveDetailResponse(self):
        try:
            genai.configure(api_key=self.KEY)
            self.model = genai.GenerativeModel('gemini-pro')
            self.chat = self.model.start_chat()
            self.responseDetail = self.chat.send_message(self.prompt)
            return self.responseDetail.text
        except Exception as e:
            return ValueError({"message":e})