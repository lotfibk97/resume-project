from allauth.account.forms import LoginForm, SignupForm
from django import forms
from datetime import date, time ,datetime
from .models import *
from .enums import note_choices


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

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'note']

class ExperienceForm(forms.ModelForm):


    class Meta:
        model = Experience
        fields = ['title','begin_date','end_date','etablissement','lieu','description']

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['begin_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})

class FormationForm(forms.ModelForm):


    class Meta:
        model = Formation
        fields = ['title','begin_date','end_date','etablissement','lieu','description']

    def __init__(self, *args, **kwargs):
        super(FormationForm, self).__init__(*args, **kwargs)
        self.fields['begin_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})


class LangueForm(forms.ModelForm):

    class Meta:
        model = Langue
        fields = ['title','note_parler','note_ecrit']
        labels = {
            "title": "Langue",
            "note_parler": "Note parler",
            "note_ecrit": "Note écrit",
        }


class HobbieForm(forms.ModelForm):

    class Meta:
        model = Hobbie
        fields = ['title']
        labels = {
            "title": "Nom de l'activité",
        }


class CvForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Cv
        fields = ['title','skills','formations','experiences','langues','hobbies']
        