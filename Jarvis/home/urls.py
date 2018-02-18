from . import views
from django.conf.urls import url

urlpatterns = [
  url(r'$^', views.index, name='index'),
  url(r'^entretenimento', views.entretenimento, name='entretenimento'),
  url(r'^saude', views.saude, name='saude'),
  url(r'^tarefas', views.tarefas, name='tarefas')
]