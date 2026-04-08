from fastapi import FastAPI
import requests

app = FastAPI()
@app.post('/v1/chat/completions')
def proxy_ollama(payload):
    return requests.post('http://localhost:11434/api/chat', json=payload).json()