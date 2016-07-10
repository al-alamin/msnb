from django import forms
from models import models
from django.db.models import Q


class FaqSearchForm(forms.Form):
    attrs = {"class": "form-control", "placeholder": "search"}
    search_item = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attrs))

    def get_search_result(self):
        item = self.cleaned_data['search_item']
        q = models.Question.objects.filter(
            Q(text__icontains=item) |
            Q(answer__text__icontains=item) |
            Q(category__name__icontains=item) |
            Q(tag__name__icontains=item)).distinct()
        return q
