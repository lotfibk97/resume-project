from django.contrib import admin
from django.urls import path, include
from core.views import homepage,signup
from django.contrib.auth import views as v

urlpatterns = [
    path('',homepage,name='homepage'),

    #path('signup/',signup,name='signup'),
    #path('login/',v.LoginView.as_view(template_name='login.html'),name='login'),
    #path('logout',v.LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]
