from django import forms

from .models import Employee, POSITION_CHOICES


class CreateAndUpdateEmployeeForm(forms.ModelForm):
    boss_id = forms.IntegerField(required=False)
    position = forms.ChoiceField(choices=POSITION_CHOICES)
    employment_at = forms.DateField(widget=forms.DateInput)

    class Meta:
        model = Employee
        exclude = ["boss"]
