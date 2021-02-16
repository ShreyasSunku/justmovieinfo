from django.urls import path
from . import views

urlpatterns = [
    path('home-page/', views.index, name='home_page'),
    path('movie-geners/<slug:language>', views.display_category, name='gener'),
    path('movie-information/<slug:mid>', views.disply_movie_info, name='movieinfo'),
    path('signup-form/', views.login_form, name='signupform'),
    path('login-form/', views.login, name='loginform'),
    path('logout/', views.logout, name='logout'),
    path('success/', views.paid, name='success'),
]