def sidebar_menu(request):
    menu = [
        {'label': 'Documentos', 'url_name': 'hub', 'icon': 'bi-folder'},
        {'label': 'Ofícios', 'url_name': 'oficios_lista', 'icon': 'bi-envelope'},
        {'label': 'Roteiros', 'url_name': 'roteiros_lista', 'icon': 'bi-map'},
        {'label': 'PT', 'url_name': 'pt_lista', 'icon': 'bi-briefcase'},
        {'label': 'OS', 'url_name': 'os_lista', 'icon': 'bi-tools'},
        {'label': 'Justificativas', 'url_name': 'justificativas_lista', 'icon': 'bi-journal-text'},
        {'label': 'Termos', 'url_name': 'termos_lista', 'icon': 'bi-file-earmark-text'},
        {'label': 'Cadastros', 'url_name': 'cadastros_home', 'icon': 'bi-people'},
        {'label': 'Configurações', 'url_name': 'admin:index', 'icon': 'bi-gear'},
    ]
    return {'sidebar_menu': menu}
