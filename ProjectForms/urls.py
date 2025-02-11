"""
URL configuration for ProjectForms project.

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
from . import views

from django.conf import settings
from django.conf.urls.static import  static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("employee/", views.employee, name="employee"),
    path("app01/", include("app01.urls")),
    path("app02/", include("app02.urls")),
    path("app03/", include("app03.urls")),
    path("app04/", include("app04.urls")),
    path("app05/", include("app05.urls")),
    path("app06/", include("app06.urls")),
    path("app07/", include("app07.urls")),
    path("app08/", include("app08.urls")),
    path("app09/", include("app09.urls")),
    path("app10/", include("app10.urls")),
    path("app11/", include("app11.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
