from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.messages import success
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from apps.users.forms import LoginUserForm, RegisterUserForm


class HomePageView(TemplateView):
    template_name = "users/index.html"


class LoginUser(LoginView):
    template_name = "users/login.html"
    form_class = LoginUserForm

    def form_valid(self, form):
        success(self.request, "Вы вошли!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tests")


def logout_user(request):
    logout(request)
    return redirect("home")


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("tests")
