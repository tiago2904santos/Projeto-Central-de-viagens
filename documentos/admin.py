from django.contrib import admin
from .models import (
    Oficio, OficioTrecho, Roteiro, RoteiroDestino, RoteiroTrecho,
    PlanoTrabalho, OrdemServico, Justificativa, TermoAutorizacao, DocumentoAvulso,
)

admin.site.register(Oficio)
admin.site.register(OficioTrecho)
admin.site.register(Roteiro)
admin.site.register(RoteiroDestino)
admin.site.register(RoteiroTrecho)
admin.site.register(PlanoTrabalho)
admin.site.register(OrdemServico)
admin.site.register(Justificativa)
admin.site.register(TermoAutorizacao)
admin.site.register(DocumentoAvulso)
