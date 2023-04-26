import requests
#from dotenv import load_dotenv
import os

#def configure():
    #load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/ayang903/ds340"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    if filename:
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    
def cleanResult(results):
    for c in results:
        c['score'] = round(c['score'] * 100)
        c['label'] = c['label'].replace("%20", ' ').title()
    return results