from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=280, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=280, widget=forms.TextInput(attrs={'class': 'form-control'}))
