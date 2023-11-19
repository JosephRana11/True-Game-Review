from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .forms import UserRegisterForm

# Create your views here.
def home_view(request):
  return render(request , 'home.html')

def game_view(request):
  return render(request , 'game.html')

def login_view(request):
  if request.method =='POST':
    print("POST recived")
    uname = request.POST['username']
    upass = request.POST['password']
    user = authenticate(username = uname , password = upass)
    if user is not None:
      login(request , user)
      print('user logged in')
      return redirect('home')
    return redirect('home')
  else:
    return render(request , 'login.html')


def logout_view(request):
  logout(request)
  return redirect('home')


def register_view(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    print(form)
    if form.is_valid():
      form.save()
      user = authenticate(username = request.POST['username'], password = request.POST['password1'])
      login(request , user)
      return redirect('home')
    else:
      return redirect('register')
  return render(request , 'register.html')