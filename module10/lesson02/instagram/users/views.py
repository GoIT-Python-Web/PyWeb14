from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm
# Create your views here.


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="app_instagram:main")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Ваш акаунт успішно створено: {username}')
            return redirect(to="users:login")

        return render(request, self.template_name, {"form": form})
