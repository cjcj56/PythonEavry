from django.db import models


class Language(models.Model):
    ENGLISH = 'en'
    HEBREW = 'he'

    RTL = 'rtl'
    LTR = 'ltr'

    LANGUAGE_CHOICES = (
        (ENGLISH,'English'),
        (HEBREW,'Hebrew'),
    )

    TEXTALIGN_CHOICES = (
        (RTL,'right'),
        (LTR,'left'),
    )

    language = models.CharField(max_length=6, choices=LANGUAGE_CHOICES,default=ENGLISH, primary_key=True)
    textalign = models.CharField(max_length=3, choices=TEXTALIGN_CHOICES, default=LTR)
    oppositealign = models.CharField(max_length=3, choices=TEXTALIGN_CHOICES, default=RTL)

    def __str__(self):
        return self.get_language_display()
        

class LessonModule(models.Model):  ## The pairs: '(module_lang,module_num)' and '(module_lang,module_name)' may be refered to as a primary key
    module_title = models.CharField(max_length=60)
    module_name = models.CharField(max_length=50,db_index=True)
    module_lang = models.ForeignKey(Language, default='en')
    module_desc = models.TextField(default='')
    module_num = models.PositiveSmallIntegerField(default=0, db_index=True) 
    module_lang.short_description = 'Module Language'
    module_desc.short_description = 'Module Description'
    module_num.short_description = 'Module Number'

    def __str__(self):
        return 'LessonModule(ID: {}, Title: {})'.format(self.module_num, self.module_title)



class Lesson(models.Model):  ## The pair: '(lesson_module,lesson_num)' may be refered to as a primary key (lang is included in module)
    lesson_title = models.CharField(max_length=60)
    lesson_desc = models.TextField()
    lesson_module = models.ForeignKey(LessonModule)
    lesson_num = models.PositiveSmallIntegerField(default=0, db_index=True)
    lesson_desc.short_description = 'Lesson Description'
    lesson_num.short_description = 'Lesson Number'

    def __str__(self):
        return "Lesson(Id: {}, Title: {})".format(str(self.lesson_num), str(self.lesson_title))

    def get_lang(self):
        return self.lesson_module.module_lang

    def get_lang_as_str(self):
        return self.lesson_module.lang.get_language_display()

    get_lang.short_description = 'Language'



class LessonVideo(models.Model):
    video_lesson = models.ForeignKey(Lesson)
    video_url = models.URLField()

    def __str__(self):
        return 'Video({})'.format(str(self.video_lesson))
    
