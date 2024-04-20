from django import forms

from .models import Employee
from .utils import POSITION_CHOICES


class CreateEmployeeForm(forms.ModelForm):
    boss_id = forms.IntegerField()
    position = forms.ChoiceField(choices=POSITION_CHOICES)
    employment_at = forms.DateField(widget=forms.DateInput)

    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "employment_at",
            "position",
            "boss_id",
        ]


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ["id"]
