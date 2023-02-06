from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                     authentication_form=LoginForm), name="login"),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
