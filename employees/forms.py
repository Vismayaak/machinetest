from django import forms
from .models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['first_name','last_name','department','designation','date_of_join','salary','image']