from fastapi import FastAPI
import uvicorn
import get_prediction
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Chat(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat-response")
def predict(chat: Chat):
    print(chat.text)
    return get_prediction.get_completion(chat.text)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)

# 3. Run the API
# uvicorn get_prediction:app --reload
