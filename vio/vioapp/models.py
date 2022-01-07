from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class User(AbstractUser):
    pass 


class Test(models.Model):
    name = models.CharField(max_length=256)
    time = models.IntegerField()
    
    def __str__(self):
        return self.name 


class Question(models.Model):
    question = RichTextUploadingField()
    right_answer = RichTextUploadingField(blank=True,
        config_name='default',
        external_plugin_resources=[(
            'youtube',
            '/staticfiles/ckeditor/ckeditor/plugins/youtube_2.1.18/youtube/',
            'plugin.js',
        )],)
    explaination = RichTextUploadingField(blank=True,
        config_name='default',
        external_plugin_resources=[(
            'youtube',
            '/staticfiles/ckeditor/ckeditor/plugins/youtube_2.1.18/youtube/',
            'plugin.js',
        )],)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE) 
    is_choice = models.BooleanField()

    def __str__(self):
        return self.question 


class Option(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = RichTextUploadingField(
        config_name='default',
        external_plugin_resources=[(
            'youtube',
            '/staticfiles/ckeditor/ckeditor/plugins/youtube_2.1.18/youtube/',
            'plugin.js',
        )],)

    def __str__(self):
        return f"Q: {self.question_id} A: {self.option}"


class Answer(models.Model): 
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE) 
    answer = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user_id} answers for {self.question_id}"
