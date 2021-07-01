from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.contrib.auth import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name='homepage'),
    path('render_pdf/<int:cv_id>',create_pdf,name='render_pdf'),
    path('cvs/',view_cvs,name='view_cvs'),
    path('profile/',view_profile,name='view_profile'),
    path('cvs/<int:cv_id>',view_single_cv,name='view_single_cv'),
    path('experiences/',view_experiences,name='view_experiences'),
    path('skills/',view_skills,name='view_skills'),
    path('languages/',view_languages,name='view_languages'),
    path('hobbies/',view_hobbies,name='view_hobbies'),
    path('formations/',view_formations,name='view_formations'),
    path('cvs/delete_cv/<int:cv_id>', delete_cv, name='delete_cv'),
    path('skills/delete_skill/<int:skill_id>', delete_skill, name='delete_skill'),
    path('formations/delete_formation/<int:formation_id>', delete_formation, name='delete_formation'),
    path('experiences/delete_experience/<int:experience_id>', delete_experience, name='delete_experience'),
    path('hobbies/delete_hobbie/<int:hobbie_id>', delete_hobbie, name='delete_hobbie'),
    path('langues/delete_langue/<int:langue_id>', delete_langue, name='delete_langue'),

    #path('signup/',signup,name='signup'),
    #path('login/',v.LoginView.as_view(template_name='login.html'),name='login'),
    #path('logout',v.LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),


    path('api/resume/<int:resume_id>', ResumeDetail.as_view(), name='resumedetail'),
    path('api/resumes/', ResumeList.as_view(), name='resumelist'),
    path('api/resume/create/', CreateResume.as_view(), name='createresume'),
    path('api/resume/edit/<int:resume_id>', EditResume.as_view(), name='editresume'),
    path('api/resume/delete/<int:resume_id>', DeleteResume.as_view(), name='deleteresume'),
    path('api/skill/<int:skill_id>', SkillDetail.as_view(), name='skilldetail'),
    path('api/skills/', SkillList.as_view(), name='skilllist'),
    path('api/skill/create/', CreateSkill.as_view(), name='createskill'),
    path('api/skill/edit/<int:skill_id>', EditSkill.as_view(), name='editskill'),
    path('api/skill/delete/<int:skill_id>', DeleteSkill.as_view(), name='deleteskill'),
    path('api/education/<int:education_id>', EducationDetail.as_view(), name='educationdetail'),
    path('api/educations/', EducationList.as_view(), name='educationlist'),
    path('api/education/create/', CreateEducation.as_view(), name='createeducation'),
    path('api/education/edit/<int:education_id>', EditEducation.as_view(), name='editeducation'),
    path('api/education/delete/<int:education_id>', DeleteEducation.as_view(), name='deleteeducation'),
    path('api/experience/<int:experience_id>', ExperienceDetail.as_view(), name='experiencedetail'),
    path('api/experiences/', ExperienceList.as_view(), name='experiencelist'),
    path('api/experience/create/', CreateExperience.as_view(), name='createexperience'),
    path('api/experience/edit/<int:experience_id>', EditExperience.as_view(), name='editexperience'),
    path('api/experience/delete/<int:experience_id>', DeleteExperience.as_view(), name='deleteexperience'),
    path('api/hobby/<int:hobby_id>', HobbyDetail.as_view(), name='hobbydetail'),
    path('api/hobbies/', HobbyList.as_view(), name='hobbylist'),
    path('api/hobby/create/', CreateHobby.as_view(), name='createhobby'),
    path('api/hobby/edit/<int:hobby_id>', EditHobby.as_view(), name='edithobby'),
    path('api/hobby/delete/<int:hobby_id>', DeleteHobby.as_view(), name='deletehobby'),
    path('api/language/<int:language_id>', LanguageDetail.as_view(), name='languagedetail'),
    path('api/languages/', LanguageList.as_view(), name='languagelist'),
    path('api/language/create/', CreateLanguage.as_view(), name='createlanguage'),
    path('api/language/edit/<int:language_id>', EditLanguage.as_view(), name='editlanguage'),
    path('api/language/delete/<int:language_id>', DeleteLanguage.as_view(), name='deletelanguage'),

]


if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)