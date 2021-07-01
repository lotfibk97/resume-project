
from rest_framework import serializers
from .models import *
from django.conf import settings


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'title', 'skills', 'experiences', 'author',
                  'languages', 'hobbies', 'educations')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'title', 'author')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'title', 'begin_date', 'end_date', 'author',
                  'facility', 'place', 'description')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'title', 'begin_date', 'end_date', 'author',
                  'facility', 'place', 'description')

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id', 'title', 'author')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'title', 'author',
                  'note_parler', 'note_ecrit')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'last_name', 'first_name', 'description',
                  'phone', 'adress' )


