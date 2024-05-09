from django import forms
from .models import Employee

# Create Add Record Form
class addEmployeeForm(forms.ModelForm):
	Nama = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"John Doe", "class":"form-control"}), label="")
	Choices  = ('Internship', 'Internship'), ('Contract', 'Contract'), ('Full-Time', 'Full Time')
	Employment_Status = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
	Monthly_Performance = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Monthly Performance", "class":"form-control"}), label="")

	class Meta:
		model = Employee
		exclude = ()