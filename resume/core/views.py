from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .forms import SkillForm,ExperienceForm,LanguageForm,HobbyForm,EducationForm,ResumeForm
import sys
from django import forms

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


import pdfkit
from django.template import loader

def create_pdf(request,cv_id):
    Resume = get_object_or_404(Resume, pk=cv_id,author=request.user.id)
    context = {'user': request.user,'Resume':Resume}
    html = loader.render_to_string('cv_tttt.html', context)
    output= pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response


def render_pdf(request, cv_id, download='0'):
    Resume = get_object_or_404(Resume, pk=cv_id,author=request.user.id)
    template_path = 'cv_test.html'
    context = {'user': request.user,'Resume':Resume}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    if download=='1':
        response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
    else:
        response['Content-Disposition'] = 'filename="Resume.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


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
    form=ResumeForm(request.POST or None)

    form.fields['skills']=forms.ModelMultipleChoiceField(queryset=Skill.objects.filter(author=request.user.id), widget=forms.CheckboxSelectMultiple)
    form.fields['languages']=forms.ModelMultipleChoiceField(queryset=Language.objects.filter(author=request.user.id), widget=forms.CheckboxSelectMultiple)
    form.fields['experiences']=forms.ModelMultipleChoiceField(queryset=Experience.objects.filter(author=request.user.id), widget=forms.CheckboxSelectMultiple)
    form.fields['formations']=forms.ModelMultipleChoiceField(queryset=Education.objects.filter(author=request.user.id), widget=forms.CheckboxSelectMultiple)
    form.fields['hobbies']=forms.ModelMultipleChoiceField(queryset=Hobby.objects.filter(author=request.user.id), widget=forms.CheckboxSelectMultiple)
    
    if form.is_valid():
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()
        form.save_m2m()

    try:
        cvs = Resume.objects.filter(author=request.user.id)

        if cvs != None:
            data = {'cvs':cvs,'form':form}
            
        else: 
            data = {'cvs':[{'title':'No cvs'}],'form':form}
            
    except ValueError:
         data = {'cvs':[{'title':'No cvs'}],'form':form}
         print("Unexpected error:", sys.exc_info()[0])
         
         
    return render(request, 'cvs.html', data)

#@login_required
#def view_langues(request):
#    form=LangueForm(request.POST or None)
#
#    if form.is_valid():
#        obj=form.save(commit=False)
#        obj.author=request.user
#        obj.save()
#
#    try:
#        langues = Language.objects.filter(author=request.user.id)
#        
#        if langues != None:
#            data = {'langues':langues,'form':form}
#            
#        else: 
#            data = {'langues':[{'title':'No langues'}],'form':form}
#            
#    except ValueError:
#         data = {'langues':[{'title':'No langues'}],'form':form}
#         print("Unexpected error:", sys.exc_info()[0])
#         
#         
#    return render(request, 'langues.html', data)
#
#
@login_required(login_url='/accounts/login')
def view_languages(request):
    """ langues of the actual user """
    languages = Language.objects.filter(author=request.user.id)
    data = {'languages':languages,  'languages_active':"active"}
    return render(request, 'langues.html', data)

@login_required(login_url='/accounts/login')
def add_language(request, user):
    """ add a language """
    if request.method == "POST":
        form = LangueForm(request.POST or None)
        
        if form.is_valid():
            """ if the form is valid """
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.success(request, "La Language a été ajouté avec succés!")
            return redirect(reverse('view_languages'))
            """ redirect to languages list """

        else:
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, error)
            return redirect(reverse("view_langues"))
            """ redirect to languages list """
    else:
        form = LangueForm()
        #print(form)
        data = {'form':form}
        return render(request, 'add_language.html', data)

@login_required(login_url='/accounts/login')
def edit_language(request,id,):
    
    try:
        language = Language.objects.get(id=id2)
        """ get the language with id = id """

        if request.method == "POST":

            form = LangueForm(request.POST or None,instance=language)

            if form.is_valid():
                """ if the form is valid """

                obj = form.save(commit=False)
                # obj.logo = request.FILES["logo"]
                obj.save()
                messages.success(request, "Les données de la Language ont été modifiées "
                                          "avec succès!")
                """ show success message """

                return redirect(reverse('view_langues'))
                """ redirect to languages list """
            else:
                """ if the form is invalid """

                for field in form:
                    if field.errors:
                        for error in field.errors:
                            messages.error(request, error)
                            """ show error message """

                return redirect(reverse("view_langues"))
                """ redirect to languages list """
        else:
            form = LangueForm(instance=languages)
            data = {'language':language,'form':form}
            return render(request, 'edit_language.html',data)

    except Language.DoesNotExist:
        """ if the doctor with id = id does not exist"""

        messages.error(request, "La Language n'existe pas")
        """ show error message """

        return redirect(reverse("view_langues"))
        """ redirect to langues list """

@login_required(login_url='/accounts/login')
def delete_language(request, id ):
    """ delete language where id = id"""

    try:
        Language = Language.objects.get(id=id)
        """ get the language with id = id """
        valid = False
        if language != None:
            valid = True
        #print(valid)
        if valid:
            """ if pressed button is Valider  """
            try:
                language.delete()
                """ delete the language """
                messages.success(request, "La Language a été supprimé avec "
                                          "succès.")
                """ show success message """
                return redirect(reverse('view_languages'))
                """ redirect to languages list """

            except Language.DoesNotExist:
                """
                if the language with id = id does not exist anymore
                """

                messages.error(request, "La Language n'existe plus")
                """ show error message """

                return redirect(reverse('view_langues'))
                """ redirect to languages list """

            

            except:
                """
                if there are other exception
                """

                messages.error(request, "Erreur lors de la suppression!")
                """ show error message """

                return redirect(reverse('view_langues'))
                """ redirect to languages list """

        data = {'language':language}
        return render(request, 'delete_language.html', data)

    except Language.DoesNotExist:
        """
        if the language with id = id does not exist
        """

        messages.error(request, "La Language n'existe pas")
        """ show error message """

        return redirect(reverse('view_languages'))
        """ redirect to languages  list """   

@login_required
def view_profile(request):

         
    return render(request, 'profile.html')


@login_required
def view_single_cv(request,cv_id):

    Resume = get_object_or_404(Resume, pk=cv_id,author=request.user.id)

    data={}
    if Resume != None:
        data={'Resume':Resume}
         
    return render(request, 'single_cv.html', data)
#
#@login_required
#def view_hobbies(request):
#    form=HobbieForm(request.POST or None)
#
#    if form.is_valid():
#        obj=form.save(commit=False)
#        obj.author=request.user
#        obj.save()
#
#    try:
#        hobbies = Hobby.objects.filter(author=request.user.id)
#        
#        if hobbies != None:
#            data = {'hobbies':hobbies,'form':form}
#            
#        else: 
#            data = {'hobbies':[{'title':'No hobbies'}],'form':form}
#            
#    except ValueError:
#         data = {'hobbies':[{'title':'No hobbies'}],'form':form}
#         print("Unexpected error:", sys.exc_info()[0])
#         
#         
#    return render(request, 'hobbies.html', data)
#
@login_required(login_url='/accounts/login')
def view_hobbies(request):
    """ hobbies of the actual user """
    hobbies = Hobby.objects.filter(author=request.user.id)
    data = {'hobbies':hobbies,  'hobbies_active':"active"}
    return render(request, 'hobbies.html', data)

@login_required(login_url='/accounts/login')
def add_hobby(request, user):
    """ add a hobby """
    if request.method == "POST":
        form = HobbieForm(request.POST or None)
        
        if form.is_valid():
            """ if the form is valid """
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.success(request, "Le Hobby a été ajouté avec succés!")
            return redirect(reverse('view_hobbies'))
            """ redirect to hobbies list """

        else:
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, error)
            return redirect(reverse("view_hobbies"))
            """ redirect to hobbies list """
    else:
        form = HobbieForm()
        #print(form)
        data = {'form':form}
        return render(request, 'add_hobby.html', data)

@login_required(login_url='/accounts/login')
def edit_hobby(request,id):
    
    try:
        hobby = Hobby.objects.get(id=id)
        """ get the hobby with id = id """

        if request.method == "POST":

            form = HobbieForm(request.POST or None,instance=hobby)

            if form.is_valid():
                """ if the form is valid """

                obj = form.save(commit=False)
                # obj.logo = request.FILES["logo"]
                obj.save()
                messages.success(request, "Les données du Hobby ont été modifiées "
                                          "avec succès!")
                """ show success message """

                return redirect(reverse('view_hobbies'))
                """ redirect to hobbies list """
            else:
                """ if the form is invalid """

                for field in form:
                    if field.errors:
                        for error in field.errors:
                            messages.error(request, error)
                            """ show error message """

                return redirect(reverse("view_hobbies"))
                """ redirect to hobbies list """
        else:
            form = HobbieForm(instance=hobby)
            data = {'hobby':hobby,'form':form}
            return render(request, 'edit_hobby.html',data)

    except Hobby.DoesNotExist:
        """ if the hobby with id = id does not exist"""

        messages.error(request, "Le Hobby n'existe pas")
        """ show error message """

        return redirect(reverse("view_hobbies"))
        """ redirect to hobbies list """

@login_required(login_url='/accounts/login')
def delete_hobby(request, id ):
    """ delete hobby where id = id"""

    try:
        hobby = Hobby.objects.get(id=id)
        """ get the hobby with id = id """
        valid = False
        if hobby != None:
            valid = True
        #print(valid)
        if valid:
            """ if pressed button is Valider  """
            try:
                hobby.delete()
                """ delete the hobby """
                messages.success(request, "Le Hobby a été supprimé avec "
                                          "succès.")
                """ show success message """
                return redirect(reverse('view_hobbies'))
                """ redirect to hobbies list """

            except Hobby.DoesNotExist:
                """
                if the hobby with id = id does not exist anymore
                """

                messages.error(request, "Le Hobby n'existe plus")
                """ show error message """

                return redirect(reverse('view_hobbies'))
                """ redirect to hobbies list """

            

            except:
                """
                if there are other exception
                """

                messages.error(request, "Erreur lors de la suppression!")
                """ show error message """

                return redirect(reverse('view_hobbies'))
                """ redirect to hobbies list """

        data = {'hobby':hobby}
        return render(request, 'delete_hobby.html', data)

    except Hobby.DoesNotExist:
        """
        if the hobby with id = id does not exist
        """

        messages.error(request, "Le Hobby n'existe pas")
        """ show error message """

        return redirect(reverse('view_hobbies'))
        """ redirect to hobbies list """   

##@login_required
##def view_experiences(request):
#    form=ExperienceForm(request.POST or None)
#
#    if form.is_valid():
#        obj=form.save(commit=False)
#        obj.author=request.user
#        obj.save()
#
#    try:
#        experiences = Experience.objects.filter(author=request.user.id)
#        
#        if experiences != None:
#            data = {'experiences':experiences,'form':form}
#            
#        else: 
#            data = {'experiences':[{'title':'No experiences'}],'form':form}
#            
#    except ValueError:
#         data = {'experiences':[{'title':'No experiences'}],'form':form}
#         print("Unexpected error:", sys.exc_info()[0])
#         
#    return render(request, 'experiences.html', data)

@login_required(login_url='/accounts/login')
def view_experiences(request):
    """ experiences of the actual user """
    experiences = Experience.objects.filter(author=request.user.id)
    data = {'experiences':experiences,  'experiences_active':"active"}
    return render(request, 'experiences.html', data)

@login_required(login_url='/accounts/login')
def add_experience(request, user):
    """ add an experience """
    if request.method == "POST":
        form = ExperienceForm(request.POST or None)
        
        if form.is_valid():
            """ if the form is valid """
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.success(request, "L'experience a été ajouté avec succés!")
            return redirect(reverse('view_experiences'))
            """ redirect to experiences list """

        else:
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, error)
            return redirect(reverse("view_experiences"))
            """ redirect to experiences list """
    else:
        form = ExperienceForm()
        #print(form)
        data = {'form':form}
        return render(request, 'add_experience.html', data)

@login_required(login_url='/accounts/login')
def edit_experience(request,id):
    
    try:
        experience = Experience.objects.get(id=id)
        """ get the skill with id = id """

        if request.method == "POST":

            form = ExperienceForm(request.POST or None,instance=experience)

            if form.is_valid():
                """ if the form is valid """

                obj = form.save(commit=False)
                # obj.logo = request.FILES["logo"]
                obj.save()
                messages.success(request, "Les données de l'experience ont été modifiées "
                                          "avec succès!")
                """ show success message """

                return redirect(reverse('view_experiences'))
                """ redirect to experiences list """
            else:
                """ if the form is invalid """

                for field in form:
                    if field.errors:
                        for error in field.errors:
                            messages.error(request, error)
                            """ show error message """

                return redirect(reverse("view_experiences"))
                """ redirect to experiences list """
        else:
            form = ExperienceForm(instance=experience)
            data = {'experience':experience,'form':form}
            return render(request, 'edit_experience.html',data)

    except Experience.DoesNotExist:
        """ if the experience with id = id does not exist"""

        messages.error(request, "L'experience n'existe pas")
        """ show error message """

        return redirect(reverse("view_experiences"))
        """ redirect to experiences list """

@login_required(login_url='/accounts/login')
def delete_experience(request, id ):
    """ delete experience where id = id"""

    try:
        experience = Experience.objects.get(id=id)
        """ get the experience with id = id """
        valid = False
        if experience != None:
            valid = True
        #print(valid)
        if valid:
            """ if pressed button is Valider  """
            try:
                experience.delete()
                """ delete the experience """
                messages.success(request, "L'experience a été supprimé avec "
                                          "succès.")
                """ show success message """
                return redirect(reverse('view_experiences'))
                """ redirect to experiences list """

            except Experience.DoesNotExist:
                """
                if the experience with id = id does not exist anymore
                """

                messages.error(request, "L'experience n'existe plus")
                """ show error message """

                return redirect(reverse('view_experiences'))
                """ redirect to experiences list """

            

            except:
                """
                if there are other exception
                """

                messages.error(request, "Erreur lors de la suppression!")
                """ show error message """

                return redirect(reverse('view_experiences'))
                """ redirect to experiences list """

        data = {'experience':experience}
        return render(request, 'delete_experience.html', data)

    except Experience.DoesNotExist:
        """
        if the experience with id = id does not exist
        """

        messages.error(request, "L'experience n'existe pas")
        """ show error message """

        return redirect(reverse('view_experiences'))
        """ redirect to experiences  list """   

#
#@login_required
#def view_formations(request):
#    form=FormationForm(request.POST or None)
#
#    if form.is_valid():
#        obj=form.save(commit=False)
#        obj.author=request.user
#        obj.save()
#
#    try:
#        formations = Education.objects.filter(author=request.user.id)
#        
#        if formations != None:
#            data = {'formations':formations,'form':form}
#            
#        else: 
#            data = {'formations':[{'title':'No formations'}],'form':form}
#            
#    except ValueError:
#         data = {'formations':[{'title':'No formations'}],'form':form}
#         print("Unexpected error:", sys.exc_info()[0])
#         
#    return render(request, 'formations.html', data)
#
#
##
@login_required(login_url='/accounts/login')
def view_formations(request):
    """ formations of the actual user """
    formations = Education.objects.filter(author=request.user.id)
    data = {'formations':formations,  'formations_active':"active"}
    return render(request, 'formations.html', data)

@login_required(login_url='/accounts/login')
def add_formation(request, user):
    """ add a Education """
    if request.method == "POST":
        form = FormationForm(request.POST or None)
        
        if form.is_valid():
            """ if the form is valid """
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.success(request, "La Education a été ajouté avec succés!")
            return redirect(reverse('view_formations'))
            """ redirect to formations list """

        else:
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, error)
            return redirect(reverse("view_formations"))
            """ redirect to formations list """
    else:
        form = FormationForm()
        #print(form)
        data = {'form':form}
        return render(request, 'add_formation.html', data)

@login_required(login_url='/accounts/login')
def edit_formation(request,id):
    
    try:
        Education = Education.objects.get(id=id)
        """ get the Education with id = id """

        if request.method == "POST":

            form = FormationForm(request.POST or None,instance=Education)

            if form.is_valid():
                """ if the form is valid """

                obj = form.save(commit=False)
                # obj.logo = request.FILES["logo"]
                obj.save()
                messages.success(request, "Les données de la Education ont été modifiées "
                                          "avec succès!")
                """ show success message """

                return redirect(reverse('view_formations'))
                """ redirect to formations list """
            else:
                """ if the form is invalid """

                for field in form:
                    if field.errors:
                        for error in field.errors:
                            messages.error(request, error)
                            """ show error message """

                return redirect(reverse("view_formations"))
                """ redirect to formations list """
        else:
            form = FormationForm(instance=Education)
            data = {'Education':Education,'form':form}
            return render(request, 'edit_formation.html',data)

    except Education.DoesNotExist:
        """ if the Education with id = id does not exist"""

        messages.error(request, "La Education n'existe pas")
        """ show error message """

        return redirect(reverse("view_formations"))
        """ redirect to formations list """

@login_required(login_url='/accounts/login')
def delete_formation(request, id ):
    """ delete Education where id = id"""

    try:
        Education = Education.objects.get(id=id)
        """ get the Education with id = id """
        valid = False
        if Education != None:
            valid = True
        #print(valid)
        if valid:
            """ if pressed button is Valider  """
            try:
                Education.delete()
                """ delete the Education """
                messages.success(request, "La Education a été supprimé avec "
                                          "succès.")
                """ show success message """
                return redirect(reverse('view_formations'))
                """ redirect to formations list """

            except Education.DoesNotExist:
                """
                if the Education with id = id does not exist anymore
                """

                messages.error(request, "La Education n'existe plus")
                """ show error message """

                return redirect(reverse('view_formations'))
                """ redirect to formations list """

            

            except:
                """
                if there are other exception
                """

                messages.error(request, "Erreur lors de la suppression!")
                """ show error message """

                return redirect(reverse('view_formations'))
                """ redirect to formations list """

        data = {'Education':Education}
        return render(request, 'delete_formation.html', data)

    except Education.DoesNotExist:
        """
        if the Education with id = id does not exist
        """

        messages.error(request, "La Education n'existe pas")
        """ show error message """

        return redirect(reverse('view_formations'))
        """ redirect to formations  list """   

##@login_required
#def view_skills(request):
#    form=SkillForm(request.POST or None)
#    
#
#    if form.is_valid():
#        obj=form.save(commit=False)
#        obj.author=request.user
#        obj.save()
#
#    try:
#        
#        skills = Skill.objects.filter(author=request.user.id)
#
#        if skills != None:
#            data = {'skills':skills,'form':form}
#            
#            
#        else: 
#            data = {'skills':[{'title':'No skills'}],'form':form}
#            
#    except ValueError:
#         data = {'skills':[{'title':'No skills'}],'form':form}
#         print("Unexpected error:", sys.exc_info()[0])
#    return render(request, 'skills.html', data)
#
@login_required(login_url='/accounts/login')
def view_skills(request):
    """ skills of the actual user """
    skills = Skill.objects.filter(author=request.user.id)
    data = {'skills':skills,  'skills_active':"active"}
    return render(request, 'skills.html', data)

@login_required(login_url='/accounts/login')
def add_skill(request, user):
    """ add a skill """
    if request.method == "POST":
        form = SkillForm(request.POST or None)
        
        if form.is_valid():
            """ if the form is valid """
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.success(request, "La compétence a été ajouté avec succés!")
            return redirect(reverse('view_skills'))
            """ redirect to skills list """

        else:
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, error)
            return redirect(reverse("view_skills"))
            """ redirect to skills list """
    else:
        form = SkillForm()
        #print(form)
        data = {'form':form}
        return render(request, 'add_skill.html', data)

@login_required(login_url='/accounts/login')
def edit_skill(request,id):
    
    try:
        skill = Skill.objects.get(id=id)
        """ get the skill with id = id """

        if request.method == "POST":

            form = SkillForm(request.POST or None,instance=skill)

            if form.is_valid():
                """ if the form is valid """

                obj = form.save(commit=False)
                # obj.logo = request.FILES["logo"]
                obj.save()
                messages.success(request, "Les données de la compétence ont été modifiées "
                                          "avec succès!")
                """ show success message """

                return redirect(reverse('view_skills'))
                """ redirect to skills list """
            else:
                """ if the form is invalid """

                for field in form:
                    if field.errors:
                        for error in field.errors:
                            messages.error(request, error)
                            """ show error message """

                return redirect(reverse("view_skills"))
                """ redirect to skills list """
        else:
            form = SkillForm(instance=skill)
            data = {'skill':skill,'form':form}
            return render(request, 'edit_skill.html',data)

    except Skill.DoesNotExist:
        """ if the doctor with id = id does not exist"""

        messages.error(request, "La compétence n'existe pas")
        """ show error message """

        return redirect(reverse("view_skills"))
        """ redirect to skills list """

@login_required(login_url='/accounts/login')
def delete_skill(request, id ):
    """ delete skill where id = id"""

    try:
        skill = Skill.objects.get(id=id)
        """ get the skill with id = id """
        valid = False
        if skill != None:
            valid = True
        #print(valid)
        if valid:
            """ if pressed button is Valider  """
            try:
                skill.delete()
                """ delete the doctor """
                messages.success(request, "La compétence a été supprimé avec "
                                          "succès.")
                """ show success message """
                return redirect(reverse('view_skills'))
                """ redirect to skills list """

            except Skill.DoesNotExist:
                """
                if the skill with id = id does not exist anymore
                """

                messages.error(request, "La compétence n'existe plus")
                """ show error message """

                return redirect(reverse('view_skills'))
                """ redirect to skills list """

            

            except:
                """
                if there are other exception
                """

                messages.error(request, "Erreur lors de la suppression!")
                """ show error message """

                return redirect(reverse('view_skills'))
                """ redirect to skills list """

        data = {'skill':skill}
        return render(request, 'healthcare/delete_skill.html', data)

    except Skill.DoesNotExist:
        """
        if the skill with id = id does not exist
        """

        messages.error(request, "La compétence n'existe pas")
        """ show error message """

        return redirect(reverse('view_skills'))
        """ redirect to skills  list """   

@login_required
def delete_cv(request,cv_id):
    Resume = get_object_or_404(Resume, pk=cv_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        Resume.delete()                     # delete the cat.
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
    Education = get_object_or_404(Education, pk=formation_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        Education.delete()                     # delete the cat.
        return redirect('/formations')             # Finally, redirect to the homepage.

    return redirect('/formations')

@login_required
def delete_hobbie(request,hobbie_id):
    Hobby = get_object_or_404(Hobby, pk=hobbie_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        Hobby.delete()                     # delete the cat.
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
    Language = get_object_or_404(Language, pk=langue_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        Language.delete()                     # delete the cat.
        return redirect('/langues')             # Finally, redirect to the homepage.

    return redirect('/langues')