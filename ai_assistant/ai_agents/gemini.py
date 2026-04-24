from google import genai
from google.genai import types
from django.conf import settings

api_key = settings.GEMINI_API_KEY

class Gemini:
    def __init__(self):
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash"
        # add this
        self.system_instruction = ("You are an expert Master Mechanic with 30 years of experience. You are helpful, safety-conscious, and practical. When asked a question:"
                                  "Always prioritize safety (e.g., 'Ensure the engine is cool before touching')."
                                  "Use professional yet accessible language. If a repair is too dangerous for a DIYer, advise they see a professional."
                                  "Keep your answers concise, encouraging. and please don't format the text in any way. Just give the answer in plain text.")
        self.system_config = types.GenerateContentConfig(
            system_instruction=self.system_instruction
        )

    def get_response(self, customer_request):
        self.system_config = types.GenerateContentConfig(
            system_instruction=self.system_instruction
        )
        
        self.chat = self.client.chats.create(
            model=self.model_name,
            config=self.system_config,
        )

        response = ""
        
        try:
            response = self.chat.send_message(customer_request)
            return response.candidates[0].content.parts[0].text
        except Exception as e:
            print(f"Error during Gemini response generation: {e}")
            return "Sorry, I'm having trouble generating a response right now. Please try again later."
