from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	Nama = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"John Doe", "class":"form-control"}), label="")
	Employment_Status = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contract", "class":"form-control"}), label="")
	Monthly_Performance = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"4200000", "class":"form-control"}), label="")

	class Meta:
		model = Employee
		exclude = ("user",)