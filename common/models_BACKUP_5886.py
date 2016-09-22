from django.contrib.auth.models import User
from django.db import models


class AuthorRole(models.Model):
    role_choices = (
        ('General', 'General'),
        ('Advisor', 'Advisor'),
        ('Reviewer', 'Reviewer'),
        ('Presenter', 'Presenter')
    )
    role = models.CharField(max_length=30,
                            choices=role_choices)

    def __str__(self):
        return self.role


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
=======

class UserMeta(models.Model):
    user = models.OneToOneField(User)
>>>>>>> 20059ba259aa5922c74ad878323577dbfe18b303
    url = models.URLField(blank=True, null=True)
    short_bio = models.TextField(max_length=200, blank=True, null=True)
    long_bio = models.TextField(max_length=5000, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    gplus_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(
                    upload_to='images/',
                    default='images/user_default.jpg')

    def __str__(self):
<<<<<<< HEAD
        return self.first_name + ' ' + self.last_name
=======
        return self.user.get_full_name()
>>>>>>> 20059ba259aa5922c74ad878323577dbfe18b303


class Type(models.Model):
    """
    It's like parent category for category and tag. eg, Visa, Higher Study
    """
    name = models.CharField(max_length=50, help_text='parent category for category and tag. eg, Visa, Higher Study')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, blank=True, null=True)

    def __str__(self):
        return self.name
<<<<<<< HEAD


class Question(models.Model):
    author = models.ForeignKey(Author)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    text = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    author = models.ForeignKey(Author)
    question = models.OneToOneField(Question)
    text = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        order_with_respect_to = 'question'


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    text = models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
def func():

    return a;

=======
>>>>>>> 20059ba259aa5922c74ad878323577dbfe18b303
