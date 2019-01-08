"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include,re_path
from app01 import views
from app02 import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('publisher_list/', views.publisher_list,name='publisher_test'),
    re_path(r'^$', views.publisher_list,name='publisher_test'),
    path('add_publisher/', views.AddPublisher.as_view()),
    # path('add_publisher/', views.add_publisher),

    path('delete_publisher/', views.delete_publisher),
    path('edit_publisher/', views.edit_publisher,name='edit_publisher'),
    #path(r'^app01/', views.book_list),
    re_path(r'^app01/', include('app01.urls')),
    path('add_book/', views.add_book),
    path('delete_book/', views.delete_book),
    path('edit_book/', views.edit_book),
    path('author_list/', views.author_list),
    path('add_author/', views.add_author),
    path('delete_author/', views.delete_author),
    path('edit_author/', views.edit_author),
    path('upload/', views.upload),
    # path('login/', login.login),
    # path('user_list/', views.user_list),
    # path('add_user/', views.add_user),

    re_path(r'^app02/',include('app02.urls')),

]










