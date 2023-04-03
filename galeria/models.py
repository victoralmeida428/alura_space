from django.db import models
import datetime as dt

class Fotografia(models.Model):
    OPCOES_CATEGORIAS = [
        ('NEBULOSA', 'Nebulosa'), 
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicado = models.BooleanField(default=False)
    data_publicado = models.DateTimeField(default=dt.datetime.now(), blank=False)


    def __str__(self) -> str:
        return f'Fotografia [nome = {self.nome}]'