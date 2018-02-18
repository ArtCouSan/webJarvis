from django.db import models

# Create your models here.
class Entretenimento(models.Model):

    entretenimento_id = models.AutoField(primary_key=True)
    entretenimento_titulo = models.CharField(max_length=100)
    entretenimento_capitulo = models.CharField(max_length=100)
    entretenimento_temporada = models.CharField(max_length=100)
    entretenimento_foto = models.CharField(max_length=100)
    entretenimento_status = models.BooleanField(verbose_name='Ativo')

class Agua(models.Model):
    
    agua_id = models.AutoField(primary_key=True)
    agua_meta = models.IntegerField()
    agua_quantidade = models.IntegerField()

class Musculacao(models.Model):

    musculacao_id = models.AutoField(primary_key=True)
    musculacao_dia = models.CharField(max_length=100)
    musculacao_treino = models.CharField(max_length=100)
    musculacao_exercicio = models.CharField(max_length=100)
    musculacao_repeticoes = models.CharField(max_length=100)
    musculacao_serie = models.CharField(max_length=100)
    musculacao_pesso = models.CharField(max_length=100)
