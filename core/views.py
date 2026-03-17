from django.contrib.auth.views import LoginView
from django.shortcuts import render


class UserLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True


def home(request):
    return render(request, 'core/home.html', {'page_title': 'Início'})
