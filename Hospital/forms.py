# Hospital/forms.py

from django import forms
from .models import Item  # Ensure the import is correct

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Use the Item model
        fields = ['name', 'description', 'price', 'quantity']  # Replace with actual fields from your Item model

        # You can customize widgets if needed, for example:
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'price': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
