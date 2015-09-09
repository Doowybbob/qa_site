from django.shortcuts import render
from .models import Question
from django.template import RequestContext, loader
from django.http import HttpResponse
# Create your views here.

def index (request):
    question_list = Question.objects.order_by('-score')[:10]
    template = loader.get_template("question_answer/index.html")
    context = RequestContext(request, {'question_list': question_list,})
    return HttpResponse(template.render(context))

