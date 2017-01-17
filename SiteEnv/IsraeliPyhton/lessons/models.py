from django.db import models


class Language(models.Model):
    lang = models.CharField(max_length=20)
    lang_code = models.CharField(max_length=6, primary_key=True)

    def __str__(self):
        return self.lang
        

# class LessonModule(models.Model):
#     module_title = models.CharField(max_length=60)
#     module_id = models.PositiveSmallIntegerField(primary_key=True, db_index=True)
#     module_lang = models.ForeignKey(Language, default="en", primary_key=True)

#     def __str__(self):
        return self.module_title


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=60)
    lesson_desc = models.TextField()
    #lesson_module = models.ForeignKey(LessonModule, primary_key=True)
    lesson_id = models.PositiveSmallIntegerField(primary_key=True, db_index=True)

    def __str__(self):
        return "".join(("Lesson_Id: ", str(self.lesson_id), ", Title: ", str(self.lesson_title)))
