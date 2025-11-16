import requests
import speech_recognition as sr
import json
from secret import client_id, client_key

def fetch_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "boolean",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()
    return data["response"]

def response_catcher(response):
    start = response.find("```json")
    end = response.find("```", start + 7)

    if start == -1 or end == -1:
        return {
            "response": response,
            "object": None
        }

    json_object = response[(start + 7):end]
    text = response[0: start]

    try:
        json_object = json.loads(json_object)
        return {
            "response": text,
            "object": json_object
        }
    except json.decoder.JSONDecodeError:
        return {
            "response": response,
            "object": None
        }

def client_respond_builder(raw_tts, ai_response, catcher_response):
    return {
        "speech": raw_tts,
        "ai_response": ai_response,
        "catcher_response": catcher_response
    }

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)
            text = r.recognize_houndify(audio, client_id, client_key)

            text = text[0]
            ai_response = fetch_ollama(text)
            cleared = response_catcher(ai_response)

            print(client_respond_builder(text, ai_response, cleared))
    except sr.UnknownValueError:
        print(sr.UnknownValueError)
        r = sr.Recognizer()
        continue