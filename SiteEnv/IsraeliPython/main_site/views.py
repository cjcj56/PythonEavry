from django.shortcuts import render
from lessons.models import LessonModule, Language
from django.shortcuts import get_object_or_404

# def welcome(request,lang):
#     textalign = ('left','right')
#     context = {
#         'lessons': Lesson.objects.all().order_by("lesson_id"),
#         'lang': lang,
#         'textalign': textalign[lang == 'he']
#     }
#     return render(request, 'main_site/' + lang + '/welcome.html', context)


def welcome(request,lang):
    lang_obj = get_object_or_404(Language, language=lang)
    context = { 
        'lesson_modules': LessonModule.objects.filter(module_lang=lang).order_by('module_num'),
        'lang': lang_obj,
    }
    return render(request, ''.join(('main_site/',lang,'/welcome.html')), context)