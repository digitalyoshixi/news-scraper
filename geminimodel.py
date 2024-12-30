import google.generativeai as genai
import os
from dotenv import load_dotenv
from webscraper import sanitizestring

load_dotenv()
geminikey = os.getenv("geminikey")

genai.configure(api_key=geminikey)

model = genai.GenerativeModel('gemini-1.5-flash')

tagwhitelist = ['AI', 'BLOCKCHAIN', 'SUSTAINABILITY', 'GENDER', 'CLOUD', 'BIG-DATA', 'GADGETS', 'FINTECH', 'EDUCATION', 'BIOMED', 'AGRICULTURE', 'CYBERSECURITY', 'POLITICS', 'SOFTWARE', 'HARDWARE', 'FIRMWARE', 'AR', 'QUANTUM', 'TECH-EVENTS', 'DEV-OPS', 'GAMING', 'IOT', 'PRIVACY', '3D-PRINTING', 'OPERATING-SYSTEM']

def get_tags(paragraph):
    modelcontent = sanitizestring(model.generate_content(f"Repond with only a list tags from the selection: {tagwhitelist} seperated by commas that are most relevant to this paragraph: {paragraph}").text.upper().strip()).split(", ")
    # mask the whitelist and returned taglist to do a last sanitize
    retlist = []
    for i in modelcontent:
        if i in tagwhitelist:
            retlist.append(i)
    return retlist

def get_summary(paragraph):
    return model.generate_content(f"Respond only with a concise 4 sentence summary of the following: {paragraph}").text
