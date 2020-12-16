from django.http import HttpResponse, Http404

from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list, 
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)
    # response = "You're at the details page of question {}."
    # return HttpResponse(response.format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    response = "You're voting on question {}."
    return HttpResponse(response.format(question_id))