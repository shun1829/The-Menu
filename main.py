from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user/")
def create_user(user: User):
    return {"res": "ok", "ID": user.user_id, "名前": user.name}


# from pydantic import BaseModel
# from fastapi import FastAPI
# import openai

# openai.api_key = "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"

# app = FastAPI()


# # リクエストボディ定義
# class Question(BaseModel):
#     content: str



# @app.post("/question")
# def question(question: Question):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": question.content},
#         ],
#     )
#     return {"answer": response.choices[0]["message"]["content"].strip()}

