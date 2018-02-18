from django.shortcuts import render
from django.http import HttpResponse
from .models import Entretenimento, Agua, Musculacao
import json

# Create your views here.
def index(request): return render(request, 'home/index.html')

def entretenimento(request):
  entretenimento = Entretenimento.objects.all()[:10]
  context = {
    'entretenimentos': entretenimento
  }
  return render(request, 'home/entretenimento.html', context)

def saude(request):
  queryset = Agua.objects.all()
  qtn = [int(obj.agua_quantidade) for obj in queryset]
  meta = [int(obj.agua_meta) for obj in queryset]
  musculacao = Musculacao.objects.all()[:10]
  context = {
    'qtn': json.dumps(qtn),
    'meta': json.dumps(meta),
    'musculacao': musculacao
  }
  return render(request, 'home/saude.html', context)


def tarefas(request):
  return render(request, 'home/tarefas.html')