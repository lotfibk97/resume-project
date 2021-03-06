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
        fields = ['title','begin_date','end_date','facility','place','description']

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['begin_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})

class EducationForm(forms.ModelForm):


    class Meta:
        model = Education
        fields = ['title','begin_date','end_date','facility','place','description']

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['begin_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ['title','note_parler','note_ecrit']
        labels = {
            "title": "Langue",
            "note_parler": "Note parler",
            "note_ecrit": "Note ??crit",
        }


class HobbyForm(forms.ModelForm):

    class Meta:
        model = Hobby
        fields = ['title']
        labels = {
            "title": "Nom de l'activit??",
        }


class ResumeForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['title','skills','educations','experiences','languages','hobbies']
        
        