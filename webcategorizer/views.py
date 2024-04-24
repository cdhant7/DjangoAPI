from django.shortcuts import render
from .utils import get_answer_from_model, fake_answer
from django.http import JsonResponse


def ask_question(request):
    q= request.GET.get("q")
    # answer = get_answer_from_model(q)
    answer = fake_answer(q)
    return JsonResponse({
        "answer": answer
    })
