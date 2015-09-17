from django.shortcuts import render, get_object_or_404
from .models import Question, Tag, Answer
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QuestionForm
from django.utils import timezone
# Create your views here.

def index (request):
    question_list = Question.objects.order_by('-score')[:10]
    template = loader.get_template("question_answer/index.html")
    context = RequestContext(request, {'question_list': question_list,})
    return HttpResponse(template.render(context))

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        answer = Answer()
        answer.answer_text = request.POST["answer_text"]
        answer.pub_date = timezone.now()
        answer.question_id = question.id
        answer.save()
    else:
        pass
    template = loader.get_template("question_answer/question.html")
    context = RequestContext(request, {'question': question,})
    return HttpResponse(template.render(context))



def ask(request):
    if request.method == "POST":

        new_q = Question()
        new_q.question_name = request.POST['QuestionName']
        new_q.question_text = request.POST['QuestionText']
        new_q.pub_date = timezone.now()
        new_q.save()
        tag_strings = request.POST['TagList']
        tag_strings = tag_strings.split(' ')

        tag_list = Tag.objects.all()
        for tag in tag_strings:
            t, created = Tag.objects.get_or_create(tag_name=tag)
            new_q.tags.add(t)

        new_q.save()

        return HttpResponseRedirect('/questions/')
    else:
        pass
    return render(request, 'question_answer/ask.html')


def add_question(request):
    #adding a new question to the db
    return HttpResponseRedirect(reverse('questions:index'))
