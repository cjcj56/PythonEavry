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
        

class LessonModule(models.Model):  ## The pairs: '(module_lang,module_num)'' and '(module_lang,module_name)'' may be refered to as a primary key
    module_title = models.CharField(max_length=60)
    module_name = models.CharField(max_length=50,db_index=True)
    module_lang = models.ForeignKey(Language, default='en')
    module_desc = models.TextField(default='')
    module_num = models.PositiveSmallIntegerField(default=0, db_index=True) 

    def __str__(self):
        return 'Module_Num: {}: Title: {}'.format(self.module_num,self.module_title)


class Lesson(models.Model):  ## The pair: '(lesson_module,lesson_num)' may be refered to as a primary key (lang is included in module)
    lesson_title = models.CharField(max_length=60)
    lesson_desc = models.TextField()
    lesson_module = models.ForeignKey(LessonModule)
    lesson_num = models.PositiveSmallIntegerField(primary_key=True, db_index=True)

    def __str__(self):
        return "".join(("Lesson_Num: ", str(self.lesson_num), ", Title: ", str(self.lesson_title)))

    def get_lang(self):
        return self.lesson_module.lang

    def get_lang_as_str(self):
        return self.lesson_module.lang.get_language_display()
