from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question', verbose_name='글쓴이')
    subject = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(verbose_name='작성일자')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일자')
    voter = models.ManyToManyField(User, related_name='voter_question', verbose_name='추천인')  # 추천인 추가
    # hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.question
    
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)