from django.urls import NoReverseMatch, reverse


def _safe_reverse(url_name, default='#'):
    try:
        return reverse(url_name)
    except NoReverseMatch:
        return default


def sidebar_menu(request):
    path = request.path or '/'

    def _is_active(prefix):
        return path == prefix or path.startswith(prefix + '/')

    items = [
        {'id': 'documentos', 'label': 'Documentos', 'icon': 'bi-folder', 'url': _safe_reverse('documentos:hub'), 'active': _is_active('/documentos')},
        {'id': 'oficios', 'label': 'Ofícios', 'icon': 'bi-envelope', 'url': _safe_reverse('documentos:oficios_lista'), 'active': _is_active('/documentos/oficios')},
        {'id': 'roteiros', 'label': 'Roteiros', 'icon': 'bi-map', 'url': _safe_reverse('documentos:roteiros_lista'), 'active': _is_active('/documentos/roteiros')},
        {'id': 'justificativas', 'label': 'Justificativas', 'icon': 'bi-journal-text', 'url': _safe_reverse('documentos:justificativas_lista'), 'active': _is_active('/documentos/justificativas')},
        {'id': 'termos', 'label': 'Termos', 'icon': 'bi-file-earmark-text', 'url': _safe_reverse('documentos:termos_lista'), 'active': _is_active('/documentos/termos')},
        {'id': 'cadastros', 'label': 'Cadastros', 'icon': 'bi-people', 'url': _safe_reverse('cadastros:cadastros_home'), 'active': _is_active('/cadastros')},
        {'id': 'config', 'label': 'Configurações', 'icon': 'bi-gear', 'url': _safe_reverse('admin:index'), 'active': _is_active('/admin')},
    ]
    return {'sidebar_menu': {'items': items}}
