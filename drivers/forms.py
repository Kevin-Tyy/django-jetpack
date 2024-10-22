from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = '__all__'


class AssignVehicleForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = ['vehicle']