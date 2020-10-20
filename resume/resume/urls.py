from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.contrib.auth import views as v

urlpatterns = [
    path('',homepage,name='homepage'),
    path('cvs/',view_cvs,name='view_cvs'),
    path('experiences/',view_experiences,name='view_experiences'),
    path('skills/',view_skills,name='view_skills'),

    #path('signup/',signup,name='signup'),
    #path('login/',v.LoginView.as_view(template_name='login.html'),name='login'),
    #path('logout',v.LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]
