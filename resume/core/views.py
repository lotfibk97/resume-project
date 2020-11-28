from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .forms import SkillForm,ExperienceForm,LangueForm,HobbieForm,HobbieForm,FormationForm,CvForm
import sys
from django import forms



def homepage(request):

    return render(request,'home.html')


def signup(request):

    form = UserCreationForm()
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request,user)
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

    return render(request,'signup.html',{'form':form})


@login_required
def view_cvs(request):
    form=CvForm(request.POST or None)

    form.fields['skills']=forms.ModelMultipleChoiceField(queryset=Skill.objects.filter(author=request.user.id), widget=forms.CheckboxSelectMultiple)

    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()
        form.save_m2m()

    try:
        cvs = Cv.objects.filter(author=request.user.id)

        if cvs != None:
            data = {'cvs':cvs,'form':form}
            
        else: 
            data = {'cvs':[{'title':'No cvs'}],'form':form}
            
    except ValueError:
         data = {'cvs':[{'title':'No cvs'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
         
         
    return render(request, 'cvs.html', data)

@login_required
def view_langues(request):
    form=LangueForm(request.POST or None)

    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()

    try:
        langues = Langue.objects.filter(author=request.user.id)
        
        if langues != None:
            data = {'langues':langues,'form':form}
            
        else: 
            data = {'langues':[{'title':'No langues'}],'form':form}
            
    except ValueError:
         data = {'langues':[{'title':'No langues'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
         
         
    return render(request, 'langues.html', data)


@login_required
def view_hobbies(request):
    form=HobbieForm(request.POST or None)

    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()

    try:
        hobbies = Hobbie.objects.filter(author=request.user.id)
        
        if hobbies != None:
            data = {'hobbies':hobbies,'form':form}
            
        else: 
            data = {'hobbies':[{'title':'No hobbies'}],'form':form}
            
    except ValueError:
         data = {'hobbies':[{'title':'No hobbies'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
         
         
    return render(request, 'hobbies.html', data)

@login_required
def view_experiences(request):
    form=ExperienceForm(request.POST or None)

    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()

    try:
        experiences = Experience.objects.filter(author=request.user.id)
        
        if experiences != None:
            data = {'experiences':experiences,'form':form}
            
        else: 
            data = {'experiences':[{'title':'No experiences'}],'form':form}
            
    except ValueError:
         data = {'experiences':[{'title':'No experiences'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
         
    return render(request, 'experiences.html', data)

@login_required
def view_formations(request):
    form=FormationForm(request.POST or None)

    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()

    try:
        formations = Formation.objects.filter(author=request.user.id)
        
        if formations != None:
            data = {'formations':formations,'form':form}
            
        else: 
            data = {'formations':[{'title':'No formations'}],'form':form}
            
    except ValueError:
         data = {'formations':[{'title':'No formations'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
         
    return render(request, 'formations.html', data)



@login_required
def view_skills(request):
    form=SkillForm(request.POST or None)
    

    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()

    try:
        
        skills = Skill.objects.filter(author=request.user.id)

        if skills != None:
            data = {'skills':skills,'form':form}
            
            
        else: 
            data = {'skills':[{'title':'No skills'}],'form':form}
            
    except ValueError:
         data = {'skills':[{'title':'No skills'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
    return render(request, 'skills.html', data)

@login_required
def delete_cv(request,cv_id):
    cv = get_object_or_404(Cv, pk=cv_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        cv.delete()                     # delete the cat.
        return redirect('/cvs')             # Finally, redirect to the homepage.

    return redirect('/cvs')


@login_required
def delete_experience(request,experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        experience.delete()                     # delete the cat.
        return redirect('/experiences')             # Finally, redirect to the homepage.

    return redirect('/exepriences')

@login_required
def delete_formation(request,formation_id):
    formation = get_object_or_404(Formation, pk=formation_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        formation.delete()                     # delete the cat.
        return redirect('/formations')             # Finally, redirect to the homepage.

    return redirect('/formations')

@login_required
def delete_hobbie(request,hobbie_id):
    hobbie = get_object_or_404(Hobbie, pk=hobbie_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        hobbie.delete()                     # delete the cat.
        return redirect('/hobbies')             # Finally, redirect to the homepage.

    return redirect('/hobbies')

@login_required
def delete_skill(request,skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        skill.delete()                     # delete the cat.
        return redirect('/skills')             # Finally, redirect to the homepage.

    return redirect('/skills')

@login_required
def delete_langue(request,langue_id):
    langue = get_object_or_404(Langue, pk=langue_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        langue.delete()                     # delete the cat.
        return redirect('/langues')             # Finally, redirect to the homepage.

    return redirect('/langues')