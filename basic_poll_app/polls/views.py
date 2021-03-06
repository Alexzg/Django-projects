from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    context = {"latest_question_list" : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {"question":question})

def results(request, question_id):
    response = "Result page: Question ID: %s" % question_id
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Voting page: Question ID: %s" % question_id)
