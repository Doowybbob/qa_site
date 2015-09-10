from django.shortcuts import render
from .models import Question
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QuestionForm
# Create your views here.

def index (request):
    question_list = Question.objects.order_by('-score')[:10]
    template = loader.get_template("question_answer/index.html")
    context = RequestContext(request, {'question_list': question_list,})
    return HttpResponse(template.render(context))

def ask(request):
    if request.method == "POST":
        return HttpResponseRedirect('/questions/')
    else:
        pass
    return render(request, 'question_answer/ask.html')


def add_question(request):
    #adding a new question to the db
    return HttpResponseRedirect(reverse('questions:index'))
