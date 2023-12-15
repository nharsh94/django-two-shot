from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': LoginForm(), 'error_message': 'Invalid'})
    else:
        return render(request, 'login.html', {'form': LoginForm()})

def user_logout(request):
    logout(request)
    return redirect("/accounts/login/")