from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def cadastros_home(request):
    context = {
        'page_title': 'Cadastros',
        'object_list': [],
    }
    return render(request, 'cadastros/home.html', context)
