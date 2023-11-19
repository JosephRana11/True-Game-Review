from django.urls import path
from pages.views import home_view , game_view , login_view , logout_view , register_view

urlpatterns = [
  path('' , home_view , name='home'),
  path('game/' , game_view , name='game'),
  path('login/' , login_view , name='login'),
  path('logout/' ,logout_view , name='logout'),
  path('register' , register_view , name = 'register')
]