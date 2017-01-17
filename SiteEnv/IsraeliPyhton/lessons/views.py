from django.shortcuts import render

def render_lesson(request,lang,lesson_module,lesson_id):
    return render(request,''.join(('lessons/', lang, '/', lesson_module, '/', lesson_id, '.html')))

