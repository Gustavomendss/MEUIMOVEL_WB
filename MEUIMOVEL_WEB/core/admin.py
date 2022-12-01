from .models import MEUIMOVELapp, Avaliacao
from django.contrib import admin
from .models import todo


@admin.register(MEUIMOVELapp)
class MEUIMOVELAdmin(admin.ModelAdmin):
    list_display = ('título', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('MEUIMOVEL', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')


admin.site.register(todo)