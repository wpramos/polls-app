from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")


def detail(request, question_id):
    response = "You're at the details page of question {}."
    return HttpResponse(response.format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    response = "You're voting on question {}."
    return HttpResponse(response.format(question_id))