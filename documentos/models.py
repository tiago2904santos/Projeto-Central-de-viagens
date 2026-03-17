from django.db import models


# ---------------------------------------------------------------------------
# Placeholder models — implementação real será feita em etapas posteriores
# ---------------------------------------------------------------------------

class Oficio(models.Model):
    numero = models.CharField('Número', max_length=50, blank=True)
    assunto = models.CharField('Assunto', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ofício'
        verbose_name_plural = 'Ofícios'
        ordering = ['-criado_em']

    def __str__(self):
        return f'Ofício {self.numero} — {self.assunto}'


class OficioTrecho(models.Model):
    oficio = models.ForeignKey(Oficio, on_delete=models.CASCADE, related_name='trechos')
    descricao = models.CharField('Descrição', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Trecho de Ofício'
        verbose_name_plural = 'Trechos de Ofício'

    def __str__(self):
        return f'Trecho do {self.oficio}'


class Roteiro(models.Model):
    titulo = models.CharField('Título', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Roteiro'
        verbose_name_plural = 'Roteiros'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


class RoteiroDestino(models.Model):
    roteiro = models.ForeignKey(Roteiro, on_delete=models.CASCADE, related_name='destinos')
    destino = models.CharField('Destino', max_length=255)

    class Meta:
        verbose_name = 'Destino de Roteiro'
        verbose_name_plural = 'Destinos de Roteiro'

    def __str__(self):
        return f'{self.destino} ({self.roteiro})'


class RoteiroTrecho(models.Model):
    roteiro = models.ForeignKey(Roteiro, on_delete=models.CASCADE, related_name='trechos')
    descricao = models.CharField('Descrição', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Trecho de Roteiro'
        verbose_name_plural = 'Trechos de Roteiro'

    def __str__(self):
        return f'Trecho do {self.roteiro}'


class PlanoTrabalho(models.Model):
    titulo = models.CharField('Título', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Plano de Trabalho'
        verbose_name_plural = 'Planos de Trabalho'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


class OrdemServico(models.Model):
    numero = models.CharField('Número', max_length=50, blank=True)
    descricao = models.CharField('Descrição', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
        ordering = ['-criado_em']

    def __str__(self):
        return f'OS {self.numero} — {self.descricao}'


class Justificativa(models.Model):
    titulo = models.CharField('Título', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Justificativa'
        verbose_name_plural = 'Justificativas'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


class TermoAutorizacao(models.Model):
    titulo = models.CharField('Título', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Termo de Autorização'
        verbose_name_plural = 'Termos de Autorização'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


class DocumentoAvulso(models.Model):
    titulo = models.CharField('Título', max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Documento Avulso'
        verbose_name_plural = 'Documentos Avulsos'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
