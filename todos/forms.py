from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadline"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                },
                format="%Y-%m-%d",
            ),
        }
