from google import genai
from google.genai import types
from django.conf import settings

api_key = settings.GEMINI_API_KEY

class Gemini:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.system_instruction = "You are a seasoned master mechanic specializing in all car types. Provide expert diagnostic advice based on codes and symptoms. and keep it short"

    def stream_response(self, customer_id, vehicle_id, issue_description):
        improved_prompt  = self.create_prompt(customer_id, vehicle_id, issue_description)

        # initHistory method implementation

        for chunk in self.chat.send_message_stream(improved_prompt):
            yield chunk.text
    
    def create_prompt(self, customer_id, vehicle_id, issue_description):
        # lets make the prompt more detailed and structured to get better responses from Gemini
        return f"Customer ID: {customer_id}, Vehicle ID: {vehicle_id}, Issue: {issue_description}"
    
    def initHistory(self, request):
        # Initialize chat history in session if not already present
        gemini_model="gemini-2.5-flash"
        system_config=types.GenerateContentConfig(
            system_instruction=self.system_instruction
        )

        self.chat = self.client.chats.create(
            model=gemini_model,
            config=system_config,
        )