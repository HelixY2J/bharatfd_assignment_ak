from django.db import models
from ckeditor.fields import RichTextField
import hashlib
from googletrans import Translator



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()
    # one for hindi and bengali

   

    def delete(self, *args, **kwargs):
        pass
        

    def __str__(self):
        return self.question
