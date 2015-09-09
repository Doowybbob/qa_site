from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date',
            'question_text',
            'question_name',
            'score']
    search_fields = ['question_name']
    list_display = ['question_name',
            'score',
            'pub_date']
    list_filter = ['pub_date']
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
