"""
URL configuration for school_management_system project.

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
from django.urls import path, include
from school_app.views import TeacherListView, StudentListView, ClassListView, SubjectListView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include([
        path('teachers/', TeacherListView.as_view(), name='teacher-list'),
        path('students/', StudentListView.as_view(), name='student-list'),
        path('classes/', ClassListView.as_view(), name='class-list'),
        path('subjects/', SubjectListView.as_view(), name='subject-list'),
   ])),
    path('', include('school_app.urls')),
]
