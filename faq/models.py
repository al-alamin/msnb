from django.db import models
from common.models import Category, Tag


# Create your models here.
class Question(models.Model):
    text = models.TextField(max_length=500)
    ans = models.TextField(max_length=500, blank=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
