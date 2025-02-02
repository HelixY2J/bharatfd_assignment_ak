from django.db import models
from ckeditor.fields import RichTextField
import hashlib
from googletrans import Translator
from django.core.cache import cache



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()
    # one for hindi and bengali
    que_hindi = models.TextField(blank=True, null=True)
    que_bengali = models.TextField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_question = self.question

    def save(self, *args, **kwargs):
        if self.question != self.original_question:
            translator = Translator()
            try:
                self.que_hindi = translator.translate(self.question, src='en', dest='hi').text
                self.que_bengali = translator.translate(self.question, src='en', dest='bn').text
            except Exception:
                self.que_hindi = self.que_bengali = None
        
        super().save(*args, **kwargs)
        self._invalidate_faqs_cache()

   

    def delete(self, *args, **kwargs):
        pass
        

    def __str__(self):
        return self.question
