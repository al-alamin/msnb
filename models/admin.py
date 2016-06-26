from django.contrib import admin
from .models import Author, Tag, Category, Questions, Answers

admin.site.register([Tag, Category, Answers])


class QuestionInLine(admin.TabularInline):
    model = Questions


class AuthorAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]


class AnswerInLine(admin.TabularInline):
    model = Answers


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Questions, QuestionAdmin)
