from django import forms
from .models import Employee

# Create Add Record Form
class addEmployeeForm(forms.ModelForm):
	Nama = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"John Doe", "class":"form-control"}), label="", initial = "awokao")
	foto = forms.ImageField(required=False)
	Choices  = ('Internship', 'Internship'), ('Contract', 'Contract'), ('Full-Time', 'Full Time')
	Employment_Status = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect, initial='Full-Time')
	Monthly_Performance = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Monthly Performance", "class":"form-control"}), label="", initial=2400000)

	class Meta:
		model = Employee
		exclude = ()