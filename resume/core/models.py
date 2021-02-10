from django.db import models
from django.conf import settings
from .enums import note_choices,type_education_choices
from django.contrib.auth.models import User




class Skill(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de la compétance")
    note = models.PositiveSmallIntegerField(default=0, choices=note_choices,blank=True,verbose_name="note de la compétance")
    class Meta:
        verbose_name = "skill"

    def __str__(self):
        return str(self.title)

class Experience(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de l'experience")
    begin_date = models.DateField(verbose_name="date de debut", null = True, blank=True)
    end_date = models.DateField(verbose_name="date de fin", null = True, blank=True)
    facility = models.CharField(max_length=100, blank =True, null=True,verbose_name="Etablissement")
    place = models.CharField(max_length=100, blank =True, null=True,verbose_name="Lieu")
    description = models.TextField(blank = True,
                            verbose_name="description", null=True)
    class Meta:
        verbose_name = "experience"
        ordering = ['begin_date']

    def __str__(self):
        return str(self.title+" "+str(self.begin_date))




class Education(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de la formation")
    begin_date = models.DateField(verbose_name="date de debut", null = True, blank=True)
    end_date = models.DateField(verbose_name="date de fin", null = True, blank=True)
    facility = models.CharField(max_length=100, blank =True, null=True,verbose_name="Etablissement")
    place = models.CharField(max_length=100, blank =True, null=True,verbose_name="Lieu")
    description = models.TextField(blank = True,
                            verbose_name="description", null=True)
    type = models.PositiveSmallIntegerField(choices=type_education_choices, default = 1, null=True, blank=True)
    class Meta:
        verbose_name = "education"
        ordering = ['begin_date']

    def __str__(self):
        return str(self.title+" "+str(self.begin_date))





class Hobby(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de l'activité")
    class Meta:
        verbose_name = "activité"
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Language(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Language")
    note_parler =  models.PositiveSmallIntegerField(default=0, choices=note_choices,blank=True,verbose_name="note parler")
    note_ecrit= models.PositiveSmallIntegerField(default=0, choices=note_choices,blank=True,verbose_name="note écrit")

    class Meta:
        verbose_name = "Language"
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    last_name = models.CharField(max_length=10, blank =True, null=True,verbose_name="nom")
    first_name = models.CharField(max_length=10, blank =True, null=True,verbose_name="prenom")
    description=models.TextField(blank=True,verbose_name='description')

    phone = models.CharField(max_length=15, blank =True, null=True,verbose_name="phone")
    adress = models.CharField(max_length=50, blank =True, null=True,verbose_name="adresse")

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return  str(self.nom) + str(self.prenom)



class Resume(models.Model):
    skills= models.ManyToManyField(Skill)
    experiences=models.ManyToManyField(Experience)
    languages=models.ManyToManyField(Language)
    hobbies=models.ManyToManyField(Hobby)
    educations=models.ManyToManyField(Education)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="title")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Resume"

    def __str__(self):
        return  self.title



