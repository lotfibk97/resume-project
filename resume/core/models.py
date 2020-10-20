from django.db import models
from django.conf import settings
from .enums import note_choices,type_formation_choices


class Experience(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de l'experience")
    begin_date = models.DateField(verbose_name="date de debut", null = True, blank=True)
    end_date = models.DateField(verbose_name="date de fin", null = True, blank=True)
    etablissement = models.CharField(max_length=100, blank =True, null=True,verbose_name="Etablissement")
    lieu = models.CharField(max_length=100, blank =True, null=True,verbose_name="Lieu")
    description = models.TextField(blank = True,
                            verbose_name="description", null=True)
    class Meta:
        verbose_name = "experience"
        ordering = ['begin_date']

    def __str__(self):
        return str(self.title+" "+str(self.begin_date))




class Formation(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de la formation")
    begin_date = models.DateField(verbose_name="date de debut", null = True, blank=True)
    end_date = models.DateField(verbose_name="date de fin", null = True, blank=True)
    etablissement = models.CharField(max_length=100, blank =True, null=True,verbose_name="Etablissement")
    lieu = models.CharField(max_length=100, blank =True, null=True,verbose_name="Lieu")
    description = models.TextField(blank = True,
                            verbose_name="description", null=True)
    type = models.PositiveSmallIntegerField(choices=type_formation_choices, default = 1, null=True, blank=True)
    class Meta:
        verbose_name = "formation"
        ordering = ['begin_date']

    def __str__(self):
        return str(self.title+" "+str(self.begin_date))

class Skill(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de la compétance")
    note = models.PositiveSmallIntegerField(default=0, choices=note_choices,blank=True,verbose_name="note de la compétance")
    class Meta:
        verbose_name = "skill"

    def __str__(self):
        return str(self.title)



class Hobbie(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="Titre de l'activité")
    class Meta:
        verbose_name = "activité"
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Langue(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank =True, null=True,verbose_name="langue")
    note_parler =  models.PositiveSmallIntegerField(default=0, choices=note_choices,blank=True,verbose_name="note parler")
    note_ecrit= models.PositiveSmallIntegerField(default=0, choices=note_choices,blank=True,verbose_name="note écrit")

    class Meta:
        verbose_name = "langue"
        ordering = ['title']

    def __str__(self):
        return str(self.title)

class Cv(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'images/', null=True, default='images/default.png')
    experiences = models.ForeignKey(Experience, on_delete=models.CASCADE)
    formations = models.ForeignKey(Formation, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    hobbies = models.ForeignKey(Hobbie, on_delete=models.CASCADE)
    langages = models.ForeignKey(Langue, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Cv"

    def __str__(self):
        return str(self.user)

