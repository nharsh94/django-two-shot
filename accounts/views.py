from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth.models import User

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

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']

            if password == password_confirmation:
                user = User.objects.create_user(
                    username = username,
                    password=password,
                )

                login(request, user)
                return redirect("home")
            else:
                form.add_error("the passwords do not match")

    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "signup.html", context)