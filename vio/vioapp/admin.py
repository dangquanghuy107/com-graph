from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Answer, Option, Question, User, Test

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Option)
admin.site.register(Test)