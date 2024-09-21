
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login_view, name='login'), 
    path('list_space', views.list_space, name='list_space'), 
    path('spaces/', views.space_list, name='space_list'),

]
