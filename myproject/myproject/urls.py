"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('foodrecipes/', views.foodrecipes),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('spaghetti/', views.spaghetti),
    path('chicken/', views.chickentikka),
    path('desserts/', views.desserts),
    path('vegetarian/', views.vegetarian),
    path('cheesecake/', views.cheesecake),
    path('vegetablestirfry/', views.vegetablestirfry),
    path('chocolatevelvetcake/', views.chocolatevelvetcake),
    path('birraatacos/', views.birriatacos),
    path('caesarsalad/', views.caesarsalad),
    path('maushroomrisotto/', views.mushroomrisotto),
    path('pancakes/', views.pancakes),
    path('shrimpfriedrice/', views.shrimpfriedrice),
    path('tiramisu/', views.tiramisu),
    path('lentil-soup/', views.lentilsoup),
    path('glazedham/', views.glazedham),
    path('pumpkinpie/', views.pumpkinpie),
    path('roastturkey/', views.roastturkey),
    path('holidays/', views.holidays),
    path('dailyrecipes/', views.dailyrecipes),
    path('breakfast/', views.breakfast),
    path('lunch/', views.lunch),
    path('dinner/', views.dinner),
    
   
]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
