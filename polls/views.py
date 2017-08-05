from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question

def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(req, 'polls/index.html', context)

def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesnotExist:
        raise Http404("Question does not exist")
    return render(req, "polls/detail.html", {'question': question})

def results(req, question_id):
    response = "Your're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
