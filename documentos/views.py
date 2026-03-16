from django.shortcuts import render
from django.contrib.auth.decorators import login_required

WIZARD_STEPS = [
    {'label': 'Dados Gerais', 'step': 1},
    {'label': 'Destinatário', 'step': 2},
    {'label': 'Trechos', 'step': 3},
    {'label': 'Revisão', 'step': 4},
    {'label': 'Justificativa', 'step': 5},
    {'label': 'Resumo', 'step': 6},
]

FILTERS_DEFAULT = {
    'status': '',
    'busca': '',
}


@login_required
def oficios_lista(request):
    context = {
        'page_title': 'Ofícios',
        'object_list': [],
        'filters': FILTERS_DEFAULT,
    }
    return render(request, 'documentos/oficios_lista.html', context)


@login_required
def oficio_step1(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Dados Gerais',
        'wizard_steps': WIZARD_STEPS,
        'current_step': 1,
    }
    return render(request, 'documentos/oficio/form_step1.html', context)


@login_required
def oficio_step2(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Destinatário',
        'wizard_steps': WIZARD_STEPS,
        'current_step': 2,
    }
    return render(request, 'documentos/oficio/form_step2.html', context)


@login_required
def oficio_step3(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Trechos',
        'wizard_steps': WIZARD_STEPS,
        'current_step': 3,
    }
    return render(request, 'documentos/oficio/form_step3.html', context)


@login_required
def oficio_step4(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Revisão',
        'wizard_steps': WIZARD_STEPS,
        'current_step': 4,
    }
    return render(request, 'documentos/oficio/form_step4.html', context)


@login_required
def oficio_justificativa(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Justificativa',
        'wizard_steps': WIZARD_STEPS,
        'current_step': 5,
    }
    return render(request, 'documentos/oficio/justificativa.html', context)


@login_required
def oficio_resumo(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Resumo',
        'wizard_steps': WIZARD_STEPS,
        'current_step': 6,
    }
    return render(request, 'documentos/oficio/resumo.html', context)


@login_required
def roteiros_lista(request):
    context = {
        'page_title': 'Roteiros',
        'object_list': [],
        'filters': FILTERS_DEFAULT,
    }
    return render(request, 'documentos/roteiros_lista.html', context)


@login_required
def pt_lista(request):
    context = {
        'page_title': 'Planos de Trabalho',
        'object_list': [],
        'filters': FILTERS_DEFAULT,
    }
    return render(request, 'documentos/pt_lista.html', context)


@login_required
def os_lista(request):
    context = {
        'page_title': 'Ordens de Serviço',
        'object_list': [],
        'filters': FILTERS_DEFAULT,
    }
    return render(request, 'documentos/os_lista.html', context)


@login_required
def justificativas_lista(request):
    context = {
        'page_title': 'Justificativas',
        'object_list': [],
        'filters': FILTERS_DEFAULT,
    }
    return render(request, 'documentos/justificativas_lista.html', context)


@login_required
def termos_lista(request):
    context = {
        'page_title': 'Termos de Autorização',
        'object_list': [],
        'filters': FILTERS_DEFAULT,
    }
    return render(request, 'documentos/termos_lista.html', context)
