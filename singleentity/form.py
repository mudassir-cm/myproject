from django import forms
from singleentity.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'