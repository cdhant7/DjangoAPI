from django.shortcuts import render
from gpt4all import GPT4All


model=GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")

def get_answer_from_model(question):
    answer = model.generate(question)
    return answer

def fake_answer(question):
    answer =" GPT RESPONSE"
    return answer