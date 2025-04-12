
from ai_generation.gemini_api import GeminiApi

_prompt_start: str = 'Please summarize the following into 2 to 3 sentences. There is no need to restate the name of the bill. Do not include anything else in your response.\n\n'

class BillSummarizer:
    def __init__(self):
        self._gemini_api = GeminiApi()
    
    def summarize(self, bill_text: str):
        return self._gemini_api.request(f'{_prompt_start}{bill_text}')
