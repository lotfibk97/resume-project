from allauth.account.forms import LoginForm, SignupForm
from django import forms

class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'input'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password','class': 'input'})

class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'input'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type':'password','class': 'input'})
        self.fields['password2'].widget = forms.TextInput(attrs={'type': 'password', 'class': 'input'})
        self.fields['email'].widget = forms.PasswordInput(attrs={'type':'email','class': 'input'})        
    

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MySignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user