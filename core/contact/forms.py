from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(max_length=500, label='Your message')