from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .forms import SkillForm
import sys




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
    try:
        cvs = Cv.objects.filter(author=request.user.id)
        if cvs != None:
            data = {'cvs':cvs}
            
        else:
            data = {'cvs':[{'title':'No cvs'}]}
    except:
        data = {'cvs':[{'title':'No cvs'}]}
    return render(request, 'cvs.html', data)

@login_required
def view_experiences(request):
    try:
        experiences = Experience.objects.filter(author=request.user.id)
        
        if experiences != None:
            data = {'experiences':experiences}
            
        else: 
            data = {'experiences':[{'title':'No experiences'}]}
            
    except:
         data = {'experiences':[{'title':'No experiences'}]}
         
    return render(request, 'experiences.html', data)



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
