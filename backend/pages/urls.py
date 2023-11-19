from django.urls import path
from pages.views import home_view , game_view , login_view

urlpatterns = [
  path('' , home_view , name='home'),
  path('game/' , game_view , name='game'),
  path('login/' , login_view , name='login'),
]