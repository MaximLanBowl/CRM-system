from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from .models import Employee


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:")


    def form_valid(self, form):
        response = super().form_valid(form)
        Employee.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class Dashboard(View):
    def dashboard(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        employee = Employee.objects.get(user=request.user)
        context = {
            'employee': employee
        }

        return render(request, 'accounts/dashboard.html', context)
