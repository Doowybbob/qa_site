from django.db import models

# Create your models here.

class Question(models.Model):
# Question model desc.
    question_name = models.CharField(max_length=200)
    question_text = models.CharField(max_length=512)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
#TODO:
#tags
#user
#comments
    def __string__ (self):
        return self.question_name

class Answer(models.Model):
# Answer model desc.
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=512)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
#TODO:
#user
#comments
