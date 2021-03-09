"""mainproject21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app21 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='main'),
    path('stu_login/',views.stulogin,name='stu_login'),
    path('sturegistration/',views.sturegistration,name='stu_registration'),
    path('stu_ForgottenPassword/',views.forgottenPassword,name='ForgottenPassword'),
    # after clicking register button url need to call this method
    path('store_inmodel/',views.storeinModel,name='store_inmodel'),

    # after student login button url need to call this function and need to
    # check password in views
    path('stu_check/',views.stucheck,name='stu_check'),
    path('stu_home/',views.stuhome,name='stu_home'),
    path('view_stuprofile/',views.view_stuprofile,name='view_stuprofile'),
    path('update_stuprofile/',views.update_stuprofile,name='update_stuprofile'),
    path('do_update/',views.doupdate,name='do_update'),
    path('show_pw/',views.showpw,name='show_pw'),

    # checking admin uname and pw
    path('admin_login/',views.adminlogin,name='admin_login'),
    path('admin_check/',views.admincheck,name='admin_check'),
    path('admin_home/',views.adminhome,name='admin_home'),
    path('view_allstudents/',views.viewallstudents,name='view_allstudents'),
    path('delete_student/',views.deletestudent,name='delete_student'),
    path('do_delete/',views.dodelete,name='do_delete')
]
