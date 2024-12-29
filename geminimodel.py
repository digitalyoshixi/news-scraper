import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
geminikey = os.getenv("geminikey")

genai.configure(api_key=geminikey)

model = genai.GenerativeModel('gemini-1.5-flash')
def get_tags(paragraph):
    return model.generate_content(f"Repond with only a list of general tags seperated by commas for this paragraph: {paragraph}").text.lower()

def get_summary(paragraph):
    return model.generate_content(f"Respond only with a concise 4 sentence summary of the following: {paragraph}").text
