"""
URL configuration for waterintake project.

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
# from django.contrib.auth.views import LoginView
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import path
from intake import views
# from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('accounts/login/', views.login_page, name='login'),
    path('add_intake/', views.add_intake, name='add_intake'),
    path('view_intakes/', views.view_intakes, name='view_intakes'),
    path('edit_intake/<int:pk>/', views.edit_intake, name='edit_intake'),    
    path('delete_intake/<int:pk>/', views.delete_intake, name='delete_intake'),
    path('list_intakes/', views.list_intakes, name='list_intakes'),
    path('find_difference/', views.find_difference, name='find_difference'),
    path('logout/', views.logout_view, name='logout'),
]
