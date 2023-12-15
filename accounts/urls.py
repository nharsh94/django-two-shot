from django.urls import path
from accounts.views import login_view, user_logout, signup

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout/', user_logout, name="logout"),
    path("signup/", signup, name="signup"),
]