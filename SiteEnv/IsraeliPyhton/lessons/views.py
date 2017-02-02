from django.shortcuts import render
from .models import Language, Lesson, LessonModule
from django.shortcuts import get_object_or_404


textalign = ('left','right')
textdir = ('ltr','rtl')

def render_index(request,lang, lesson_module_name):
    #lesson_module = LessonModule.objects.get(module_name=lesson_module_name,module_lang=lang)
    lang_obj = get_object_or_404(Language, language=lang)
    lesson_module = get_object_or_404(LessonModule,module_name=lesson_module_name,module_lang=lang_obj)
    lessons = Lesson.objects.filter(lesson_module=lesson_module).order_by('lesson_num')
    textalign = ('left','right')
    context = { 
        'lang': lang_obj,
        'lessons': lessons,
        'lesson_module': lesson_module,
    }
    return render(request, ''.join(('lessons/',lang,'/', lesson_module.module_name,'/index.html')), context)


# def render_lesson(request,lang,lesson_module,lesson_num,lesson_type):
def render_lesson(request,lang,lesson_module_name,lesson_num):
    # lesson_module = LessonModule.objects.get(module_name=lesson_module_name,module_lang=lang)
    # lesson = Lesson.objects.get(lesson_num=lesson_num,lesson_module=lesson_module)
    lang_obj = get_object_or_404(Language, language=lang)
    lesson_module = get_object_or_404(LessonModule, module_name=lesson_module_name,module_lang=lang_obj)
    lesson = get_object_or_404(Lesson, lesson_num=lesson_num,lesson_module=lesson_module)
    # context = {'lang': lang, 'lesson_module': lesson_module, 'lesson_id': lesson_num, 'lesson': lesson[0], 'lesson_type': lesson_type }
    context = {
        'lang': lang_obj,
        'lesson_module': lesson_module,
        'lesson': lesson,
    }
    # return render(request,''.join(('lessons/', lang, '/', lesson_module_name, '/', lesson_num, '_', lesson_type, '.html')), context)
    return render(request,''.join(('lessons/', lang, '/', lesson_module_name, '/', lesson_num, '.html')), context)

