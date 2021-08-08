from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.contrib.auth import views as v
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view 

urlpatterns = [
    

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
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),

]


if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)