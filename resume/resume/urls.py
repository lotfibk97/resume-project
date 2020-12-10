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
    path('langues/',view_langues,name='view_langues'),
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


]


if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)