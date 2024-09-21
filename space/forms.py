from django import forms
from .models import ParkingSpace

class ParkingSpaceForm(forms.ModelForm):
    class Meta:
        model = ParkingSpace
        fields = ['space_name', 'location', 'price', 'availability'] 
