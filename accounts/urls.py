from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    RegisterView,
    LogoutPage,
    Dashboard,


)

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True),
         name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

]
