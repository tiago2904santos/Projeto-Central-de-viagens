from django.shortcuts import render


def cadastros_home(request):
    return render(request, 'core/home.html', {'page_title': 'Cadastros'})
