from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    #message = forms.CharField(widget=forms.Textarea)



class SigninForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    

    