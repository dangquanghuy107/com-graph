from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Option, Question, Test

import json


def get_question(request):
    test_id = request.GET.get('test_id', '')
    questions = Question.objects.filter(test_id=test_id)
    questions = json.loads(serializers.serialize('json', questions))
    return JsonResponse({'questions': questions})


def get_option(request):
    question_id = request.GET.get('id', '')
    options = Option.objects.filter(question_id=question_id)
    options = json.loads(serializers.serialize('json', options))
    return JsonResponse({'options': options})


def get_test_info(request):
    test_id = request.GET.get('test_id', '')
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test_id=test_id)
    questions = json.loads(serializers.serialize('json', questions))
    return JsonResponse(
        {
            'time': test.time,
            'n_ques': len(questions)
        })