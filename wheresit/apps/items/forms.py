from django.forms import Form, ModelForm
from django import forms
from models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item

class ItemSearchForm(Form):
    name_search = forms.CharField(max_length=100, required=False)
    tags_search = forms.CharField(max_length=100, required=False)
