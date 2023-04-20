"""
URL configuration for myLMS project.

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
from django.contrib import admin
from django.urls import path, re_path
from user.views import vw_login, vw_logout, vw_home
from course.views import vw_course_list, vw_course_register, vw_department_list, vw_department_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', vw_login),
    path('logout/', vw_logout),
    path('home/', vw_home),
    path('',vw_home),
    path('course-list/',vw_course_list),
    path('course-register/',vw_course_register),
    path('department-list/',vw_department_list),
    re_path('^department-list/(\d+)/$',vw_department_info),

]
