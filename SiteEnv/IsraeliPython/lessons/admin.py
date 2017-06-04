from django.contrib import admin
from .models import Language, LessonModule, Lesson, LessonVideo

admin.site.register(Language)
# admin.site.register(LessonModule)
# admin.site.register(Lesson)
admin.site.register(LessonVideo)


class LessonModuleAdmin(admin.ModelAdmin):
    list_display = ('module_num', 'module_title', 'module_desc')
    list_filter = ('module_lang',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_module', 'lesson_num', 'lesson_title', 'lesson_desc')
    list_filter = ('lesson_module', 'lesson_module__module_lang')


admin.site.register(LessonModule, LessonModuleAdmin)
admin.site.register(Lesson, LessonAdmin)
