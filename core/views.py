from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def redirect_to_hub(request):
    return redirect('hub')


@login_required
def hub(request):
    context = {
        'page_title': 'Hub de Documentos',
        'quick_report': {
            'oficios': 0,
            'roteiros': 0,
            'pt': 0,
            'os': 0,
            'justificativas': 0,
            'termos': 0,
        },
    }
    return render(request, 'documentos/hub.html', context)
