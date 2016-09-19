from django.contrib import admin

from common.models import Tag, Category, Type, UserMeta

admin.site.register([Tag, Category, UserMeta])


class TagInline(admin.TabularInline):
    model = Tag


class CategoryInline(admin.TabularInline):
    model = Category


class TypeAdmin(admin.ModelAdmin):
    inlines = [TagInline, CategoryInline]


admin.site.register(Type, TypeAdmin)
