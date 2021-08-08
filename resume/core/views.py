from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .forms import SkillForm, ExperienceForm, LanguageForm, HobbyForm, EducationForm, ResumeForm
import sys
from django import forms

from .models import *
from .serializers import *
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
#from xhtml2pdf import pisa


#import pdfkit
from django.template import loader


def signup(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)
            return redirect(reverse('homepage'))

        else:
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, error)
                        print("erreurrrrrrr")
                        print(error)
            return redirect(reverse('homepage'))

    else:
        form = UserCreationForm()

        print("cccccccccccc")

    return render(request, 'signup.html', {'form': form})


# @login_required(login_url='/accounts/login')
class LanguageDetail(generics.RetrieveAPIView):

    serializer_class = LanguageSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('language_id')
        return get_object_or_404(Language, id=item)

# @login_required(login_url='/accounts/login')


class CreateLanguage(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


# @login_required(login_url='/accounts/login')
class EditLanguage(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    lookup_url_kwarg = 'language_id'

# @login_required(login_url='/accounts/login')


class DeleteLanguage(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    lookup_url_kwarg = 'language_id'

# @login_required


class ProfileDetail(generics.RetrieveAPIView):

    serializer_class = ProfileSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('profile_id')
        return get_object_or_404(Profile, id=item)


class ResumeDetail(generics.RetrieveAPIView):

    serializer_class = ResumeSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('resume_id')
        return get_object_or_404(Resume, id=item)


# @login_required(login_url='/accounts/login')
class HobbyList(generics.ListAPIView):
    # def hobby(self, request):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HobbySerializer

    def get_queryset(self):
        return Hobby.objects.filter(author=self.request.user)

# @login_required(login_url='/accounts/login')


class CreateHobby(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

# @login_required


class EditHobby(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()
    lookup_url_kwarg = 'hobby_id'
# @login_required


class DeleteHobby(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()
    lookup_url_kwarg = 'hobby_id'

# @login_required


class ExperienceDetail(generics.RetrieveAPIView):

    serializer_class = ExperienceSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('experience_id')
        return get_object_or_404(Experience, id=item)

# @login_required(login_url='/accounts/login')


class ExperienceList(generics.ListAPIView):
    # def experience(self, request):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        print(self.request)
        return Experience.objects.filter(author=self.request.user)

# @login_required(login_url='/accounts/login')


class CreateExperience(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

# @login_required


class EditExperience(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    lookup_url_kwarg = 'experience_id'
# @login_required


class DeleteExperience(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    lookup_url_kwarg = 'experience_id'

# @login_required


class EducationDetail(generics.RetrieveAPIView):

    serializer_class = EducationSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('education_id')
        return get_object_or_404(Education, id=item)

# @login_required(login_url='/accounts/login')


class EducationList(generics.ListAPIView):
    # def education(self, request):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        return Education.objects.filter(author=self.request.user)

# @login_required(login_url='/accounts/login')


class CreateEducation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

# @login_required


class EditEducation(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    lookup_url_kwarg = 'education_id'
# @login_required


class DeleteEducation(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    lookup_url_kwarg = 'education_id'

# @login_required


class SkillDetail(generics.RetrieveAPIView):

    serializer_class = SkillSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('skill_id')
        print(self.kwargs)
        return get_object_or_404(Skill, id=item)

# @login_required(login_url='/accounts/login')


class SkillList(generics.ListAPIView):
    # def skill(self, request):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.filter(author=self.request.user)

# @login_required(login_url='/accounts/login')


class CreateSkill(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# @login_required


class EditSkill(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    lookup_url_kwarg = 'skill_id'


# @login_required
class DeleteSkill(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    lookup_url_kwarg = 'skill_id'

# @login_required


class ResumeDetail(generics.RetrieveAPIView):

    serializer_class = ResumeSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('resume_id')
        return get_object_or_404(Resume, id=item)

# @login_required(login_url='/accounts/login')


class ResumeList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(author=self.request.user)


# @login_required(login_url='/accounts/login')
class CreateResume(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

# @login_required


class EditResume(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    lookup_url_kwarg = 'resume_id'
# @login_required


class DeleteResume(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    lookup_url_kwarg = 'resume_id'


class HobbyDetail(generics.RetrieveAPIView):

    serializer_class = HobbySerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('hobby_id')
        return get_object_or_404(Hobby, id=item)


class LanguageList(generics.ListAPIView):
    #    def resume(self, request):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
