from django.contrib import admin
from .models import Language, LessonModule, Lesson

admin.site.register(Language)
admin.site.register(LessonModule)
admin.site.register(Lesson)