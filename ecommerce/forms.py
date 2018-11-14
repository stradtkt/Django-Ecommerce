from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Your Full Name", "id": "contact_name"}))
    email     = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Email", "id": "contact_email"}))
    content  = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message", "id": "contact_message"}))