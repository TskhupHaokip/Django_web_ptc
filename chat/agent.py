from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class Agent:
    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.chat = self.client.chats.create(
            model="gemini-3.5-flash-lite"
        )

    def stream(self,message:str):
        response = self.chat.send_message_stream(
            message=message
        )
       
        for chunk in response:
            if chunk.text:
                yield chunk.text

if __name__ == '__main__':
    pass
