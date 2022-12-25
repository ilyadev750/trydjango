from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'age',
            'city',
            'sex'
        ]

class RawUserForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "name"
    }))
    last_name = forms.CharField(label='Last name')
    age = forms.IntegerField()
    city = forms.CharField(widget=forms.Textarea(attrs={
        "class": "new class",
        "placeholder": "description",
        "rows": 20,
        "cols": 10
    }))
    sex = forms.CharField(required=False)