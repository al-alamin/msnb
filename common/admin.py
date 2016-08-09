from django.contrib import admin

from common.models import Author, Tag, Category, Question, Answer, Post, Type, AuthorRole

admin.site.register([Tag, Category, Answer, Post, AuthorRole])


class TagInline(admin.TabularInline):
    model = Tag


class CategoryInline(admin.TabularInline):
    model = Category


class TypeAdmin(admin.ModelAdmin):
    inlines = [TagInline, CategoryInline]


class QuestionInLine(admin.TabularInline):
    model = Question


class AuthorAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Type, TypeAdmin)

