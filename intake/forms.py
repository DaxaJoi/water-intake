from django import forms
from .models import WaterIntake

class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = WaterIntake
        fields = ['quantity']

class DateRangeForm(forms.Form):
    date1 = forms.DateField(widget=forms.SelectDateWidget)
    date2 = forms.DateField(widget=forms.SelectDateWidget)
