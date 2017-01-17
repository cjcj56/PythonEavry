from django.shortcuts import render
from lessons.models import Lesson

def welcome(request,lang):
    textalign = ('left','right')
    context = {
        'lessons': Lesson.objects.all().order_by("lesson_id"),
        'lang': lang,
        'textalign': textalign[lang == 'he']
    }
    return render(request, 'main_site/' + lang + '/welcome.html', context)

