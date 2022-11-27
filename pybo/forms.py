from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from .models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    # content =SummernoteTextField()
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets = {'content' : SummernoteWidget()}
        labels = {
            'subject': '제목',
            'content': '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }