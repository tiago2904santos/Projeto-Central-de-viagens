from django import forms
from django.shortcuts import render
from django.urls import reverse


def _wizard_steps(current_step):
    steps = [
        {'id': 1, 'label': 'Dados e viajantes', 'url': reverse('documentos:oficio_step1')},
        {'id': 2, 'label': 'Transporte', 'url': reverse('documentos:oficio_step2')},
        {'id': 3, 'label': 'Roteiro e diárias', 'url': reverse('documentos:oficio_step3')},
        {'id': 4, 'label': 'Resumo', 'url': reverse('documentos:oficio_step4')},
        {'id': 5, 'label': 'Justificativa', 'url': reverse('documentos:oficio_justificativa')},
    ]
    for step in steps:
        step['active'] = step['id'] == current_step
    return steps


def _quick_report():
    return {
        'oficio': '-',
        'protocolo': '-',
        'data_criacao': '-',
        'situacao_origem': '-',
        'motivo': '-',
        'viajantes': '-',
        'responsavel': '-',
        'motorista': '-',
        'veiculo': '-',
        'placa': '-',
        'modelo': '-',
        'combustivel': '-',
        'tipo_viatura': '-',
        'carona_oficio': '-',
        'roteiro_modo': '-',
        'roteiro_fonte': 'Roteiro próprio',
        'periodo': '-',
        'destino_principal': '-',
        'justificativa_required': '-',
        'justificativa': '-',
        'diarias_qtd': '-',
        'diarias_valor': '-',
        'diarias_extenso': '-',
    }


def _base_filters():
    return {
        'q': '',
        'status': '',
        'tipo': '',
        'ano': '',
        'numero': '',
        'protocolo': '',
        'destino': '',
    }


class Step1MockForm(forms.Form):
    oficio_numero = forms.CharField(required=False)
    protocolo = forms.CharField(required=False)
    data_criacao = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    modelo_motivo = forms.ChoiceField(required=False, choices=[('', '---------')])
    motivo = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
    custeio_tipo = forms.ChoiceField(required=False, choices=[('', '---------'), ('ORGAO', 'Órgão'), ('OUTRA_INSTITUICAO', 'Outra instituição')])
    nome_instituicao_custeio = forms.CharField(required=False)
    viajantes = forms.CharField(required=False)


class Step2MockForm(forms.Form):
    placa = forms.CharField(required=False)
    modelo = forms.CharField(required=False)
    combustivel = forms.CharField(required=False)
    tipo_viatura = forms.ChoiceField(required=False, choices=[('', '---------')])
    porte_transporte_armas = forms.ChoiceField(required=False, choices=[('', '---------'), ('NAO', 'Não'), ('SIM', 'Sim')])
    motorista_viajante = forms.CharField(required=False)
    motorista_oficio_ano = forms.CharField(required=False, initial='2026')
    motorista_oficio_numero = forms.CharField(required=False)
    motorista_protocolo = forms.CharField(required=False)
    motorista_nome = forms.CharField(required=False)


class JustificativaMockForm(forms.Form):
    modelo_justificativa = forms.ChoiceField(required=False, choices=[('', '---------')])
    justificativa_texto = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 8}))


def hub(request):
    context = {
        'page_title': 'Documentos',
        'cards': [
            {'label': 'Ofícios', 'description': 'Gestão completa dos ofícios.', 'count': 0, 'url': reverse('documentos:oficios_lista')},
            {'label': 'Roteiros', 'description': 'Biblioteca de roteiros independentes.', 'count': 0, 'url': reverse('documentos:roteiros_lista')},
            {'label': 'Justificativas', 'description': 'Acompanhamento das justificativas.', 'count': 0, 'url': reverse('documentos:justificativas_lista')},
            {'label': 'Termos', 'description': 'Central de termos de autorização.', 'count': 0, 'url': reverse('documentos:termos_lista')},
        ],
        'quick_report': _quick_report(),
    }
    return render(request, 'documentos/hub.html', context)


def oficios_lista(request):
    context = {
        'page_title': 'Ofícios',
        'object_list': [],
        'filters': _base_filters(),
        'status_choices': [('RASCUNHO', 'Rascunho'), ('FINALIZADO', 'Finalizado')],
        'quick_report': _quick_report(),
    }
    return render(request, 'documentos/oficios_lista.html', context)


def oficio_step1(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Dados e viajantes',
        'wizard_steps': _wizard_steps(1),
        'form': Step1MockForm(),
        'selected_viajantes': [],
        'selected_viajantes_payload': [],
        'buscar_viajantes_url': '#',
        'cadastrar_viajante_url': '#',
        'gerenciar_modelos_motivo_url': '#',
        'modelo_texto_api_pattern': '/documentos/modelos-motivo/0/',
        'step1_preview': {'data_criacao': '-'},
        'quick_report': _quick_report(),
    }
    return render(request, 'documentos/oficio/wizard_step1.html', context)


def oficio_step2(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Transporte',
        'wizard_steps': _wizard_steps(2),
        'form': Step2MockForm(),
        'step1_preview': {'oficio': '-', 'protocolo': '-', 'data_criacao': '-', 'motivo': '-', 'custeio': '-'},
        'step2_preview': {
            'placa': '-',
            'modelo': '-',
            'combustivel': '-',
            'tipo_viatura_label': '-',
            'porte_transporte_armas_label': '-',
            'motorista': {'has_value': False, 'nome_display': '-'},
            'veiculo_lookup': {'found': False, 'message': 'Digite a placa para localizar a viatura ou preencha manualmente.'},
        },
        'selected_viajantes': [],
        'selected_motorista_payload': None,
        'combustivel_opcoes': [],
        'mostrar_campos_carona': False,
        'mostrar_motorista_manual': False,
        'motorista_sem_cadastro_value': 'SEM_CADASTRO',
        'motorista_oficio_ano_display': '2026',
        'buscar_veiculos_url': '#',
        'buscar_veiculo_url': '#',
        'buscar_motoristas_url': '#',
        'cadastrar_veiculo_url': '#',
        'cadastrar_viajante_url': '#',
        'oficio_viajantes_ids_csv': '',
        'quick_report': _quick_report(),
    }
    return render(request, 'documentos/oficio/wizard_step2.html', context)


def oficio_step3(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Roteiro e diárias',
        'wizard_steps': _wizard_steps(3),
        'quick_report': _quick_report(),
        'validation_errors': [],
        'step3_seed_source_label': '',
        'roteiro_modo': 'ROTEIRO_PROPRIO',
        'has_event_routes': False,
        'roteiros_evento': [],
        'roteiro_evento_id': '',
        'estados': [],
        'sede_estado_id': '',
        'sede_cidade_id': '',
        'sede_cidades_qs': [],
        'retorno_state': {
            'saida_cidade': '',
            'chegada_cidade': '',
            'saida_data': '',
            'saida_hora': '',
            'chegada_data': '',
            'chegada_hora': '',
            'distancia_km': '',
            'duracao_estimada_min': '',
            'tempo_cru_estimado_min': '',
            'tempo_adicional_min': 0,
            'rota_fonte': '',
        },
        'step3_preview': {
            'tipo_destino': '-',
            'roteiro_modo_label': 'Montar roteiro neste ofício',
            'roteiro_evento_label': '',
            'diarias': {'quantidade': '-', 'valor_total': '-', 'valor_extenso': '-'},
            'tem_trechos': False,
            'trechos': [],
            'retorno': {'show': False},
        },
        'step3_diarias_resultado': None,
        'step3_state_json': {
            'roteiro_modo': 'ROTEIRO_PROPRIO',
            'destinos_atuais': [{'estado_id': None, 'cidade_id': None}],
            'trechos': [],
            'retorno': {},
        },
        'roteiros_evento_json': [],
        'api_cidades_por_estado_url': '/documentos/api/estados/0/cidades/',
        'api_estimar_trecho_url': '#',
        'api_calcular_diarias_url': '#',
        'destino_estado_fixo_id': '',
        'destino_estado_fixo_nome': 'Paraná (PR)',
    }
    return render(request, 'documentos/oficio/wizard_step3.html', context)


def oficio_step4(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Resumo',
        'wizard_steps': _wizard_steps(4),
        'quick_report': _quick_report(),
        'finalize_validation': {'sections': []},
        'oficio': {
            'numero_formatado': '-',
            'protocolo_formatado': '-',
            'status': 'RASCUNHO',
            'get_status_display': 'Rascunho',
            'motivo': '-',
            'motorista_oficio_formatado': '-',
            'motorista_protocolo_formatado': '-',
            'gerar_termo_preenchido': False,
            'justificativa_texto': '',
        },
        'selected_viajantes': [],
        'step1_preview': {'custeio': '-'},
        'step2_preview': {'placa': '-', 'modelo': '-', 'combustivel': '-', 'tipo_viatura_label': '-', 'motorista': {'nome_display': '-'}},
        'step3_preview': {
            'roteiro_modo_label': '-',
            'roteiro_evento_label': '',
            'tipo_destino': '-',
            'diarias': {'quantidade': '-', 'valor_total': '-', 'valor_extenso': '-'},
            'tem_trechos': False,
            'trechos': [],
            'retorno': {'show': False},
        },
        'justificativa_info': {'status_label': '-', 'prazo_minimo_dias': 0, 'primeira_saida_display': '-'},
        'termo_autorizacao': {'available': False, 'actions': [], 'errors': []},
        'oficio_downloads': {'actions': [], 'errors': []},
        'justificativa_url': reverse('documentos:oficio_justificativa'),
    }
    return render(request, 'documentos/oficio/wizard_step4.html', context)


def oficio_justificativa(request):
    context = {
        'page_title': 'Novo Ofício',
        'wizard_page_title': 'Justificativa',
        'wizard_steps': _wizard_steps(5),
        'form': JustificativaMockForm(),
        'quick_report': _quick_report(),
        'modelos_justificativa_url': '#',
        'voltar_step4_url': reverse('documentos:oficio_step4'),
        'next_url': reverse('documentos:oficio_step4'),
        'modelos_justificativa_texto_api_pattern': '/documentos/modelos-justificativa/0/texto/',
    }
    return render(request, 'documentos/oficio/justificativa.html', context)


def oficio_resumo(request):
    return oficio_step4(request)


def roteiros_lista(request):
    context = {
        'page_title': 'Roteiros',
        'object_list': [],
        'filters': _base_filters(),
        'status_choices': [('RASCUNHO', 'Rascunho'), ('FINALIZADO', 'Finalizado')],
        'tipo_choices': [('', 'Todos'), ('PADRAO', 'Padrão')],
        'novo_roteiro_url': '#',
        'novo_roteiro_url_floating': '#',
    }
    return render(request, 'documentos/roteiros_lista.html', context)


def justificativas_lista(request):
    context = {
        'page_title': 'Justificativas',
        'object_list': [],
        'filters': _base_filters(),
        'status_choices': [('PENDENTE', 'Pendente'), ('PREENCHIDA', 'Preenchida')],
    }
    return render(request, 'documentos/justificativas_lista.html', context)


def termos_lista(request):
    context = {
        'page_title': 'Termos',
        'object_list': [],
        'filters': _base_filters(),
        'status_choices': [('PENDENTE', 'Pendente'), ('CONCLUIDO', 'Concluído')],
    }
    return render(request, 'documentos/termos_lista.html', context)
