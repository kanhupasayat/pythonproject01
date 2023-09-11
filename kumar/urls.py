"""
URL configuration for kumar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from multiprocessing.context import _force_start_method
from django.contrib import admin
from django.urls import path
from django.urls import path
from student.views import *
from django.contrib.auth.views import PasswordResetView





from re import template
from tempfile import tempdir
from django.contrib import admin
from django.urls import path
from student import views
from student.views import *
from django.urls import path, include  # Import 'include'

from student.views import *  # Import your existing views
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.urls import path


from django.contrib.staticfiles.urls import staticfiles_urlpatterns


    



urlpatterns = [
    path('student/', student, name='student'),
    path('', login_page, name='login_page'),
    path('index/', index_page, name='index_page'),
    path('index2/', index2_page, name='index2_page'),
    
    path('index/show/', show_page, name='show_page'),
    path('show/', show_page, name='show_page'),
    path('index/show/search_page/', search_page, name='search_page'),
    path('show/search_page/', search_page, name='search_page'),
    path('logout/', logout_page, name='logout_page'),
    path('student-list/',student_list, name='student_list'),
    path('user_list/',user_list, name='user_list'),
    path('user_list/show_data/',show_data, name='show_data'),
    path('show_data/',show_data, name='show_data'),
    path('user_detail/<str:username>/',user_detail, name='user_detail'),


#==========delete user========


path('delete_user/<str:username>/', views.delete_user, name='delete_user'),



#========update user =first name last_name and email=======

path('update_user/<str:username>/', views.update_user, name='update_user'),



    




    



    #==========change password======
    path('ChangePassword',views.Change_Password,name='changepassword'),


#===========forgot_password======

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('admin/', admin.site.urls),



    #======admin login 

    path('export/', views.export_data_to_excel, name='export_data_to_excel'),
    path('export_data_to_excel2/', views.export_data_to_excel2, name='export_data_to_excel2'),


]


urlpatterns+=staticfiles_urlpatterns()














