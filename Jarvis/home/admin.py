from django.contrib import admin
# Register your models here.
from home.models import Entretenimento
from home.models import Agua, Musculacao
# Register your models here.
class EntretenimentoAdmin(admin.ModelAdmin):
    model: Entretenimento
    list_display = ['entretenimento_titulo', 'entretenimento_capitulo', 'entretenimento_temporada', 'entretenimento_foto', 'entretenimento_status']
    search_field = ['entretenimento_titulo']
    save_on_top = True

admin.site.register(Entretenimento, EntretenimentoAdmin)

class AguaAdmin(admin.ModelAdmin):
    model: Agua
    list_display = ['agua_id', 'agua_meta', 'agua_quantidade']
    search_field = ['agua_id']
    save_on_top = True

admin.site.register(Agua, AguaAdmin)

class MusculacaoAdmin(admin.ModelAdmin):
    model: Musculacao
    list_display = ['musculacao_id', 'musculacao_dia', 'musculacao_treino', 'musculacao_exercicio', 'musculacao_repeticoes', 'musculacao_serie', 'musculacao_pesso']
    search_field = ['musculacao_dia']
    save_on_top = True

admin.site.register(Musculacao, MusculacaoAdmin)
