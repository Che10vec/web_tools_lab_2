from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User

# Create your views here.
def user_view(request):

    if request.method == "POST":
        data = request.POST
        action = data.get("button")
        if action == "Delete":
            try:
                request.user.delete()
            except Exception as e:
                None
            return redirect('user')
        elif action == "Sign out":
            logout(request)
    return render(request, 'user.html')

def authorize_u_view(request):
    message =None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('user')
            else:
                message = 'No such user'
    else:
        form = LoginForm()
    return render(request, 'authorize_u.html',{'form': form,'message': message})

def create_u_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('user')
    else:
        form = SignupForm()
    return render(request, 'create_u.html',{'form': form})
