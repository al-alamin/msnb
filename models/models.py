from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    url = models.URLField()
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
