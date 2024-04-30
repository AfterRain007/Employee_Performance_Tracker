from django import forms
from .models import Employee

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	Nama = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"John Doe", "class":"form-control"}), label="")
	GEEKS_CHOICES  = ('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')
	Employment_Status = forms.ChoiceField(choices=GEEKS_CHOICES, widget=forms.RadioSelect)
	Monthly_Performance = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Monthly Performance", "class":"form-control"}), label="")

	class Meta:
		model = Employee
		exclude = ("user",)