
from google import genai

_api_key: str = 'AIzaSyDVP-mXMtISINX0BFAdvM_jg-vLCtjR75Y'

class GeminiApi:
    def __init__(self):
        self._genai_client = genai.Client(api_key=_api_key)
    
    def request(self, prompt: str):
        response = self._genai_client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
        return response.text
