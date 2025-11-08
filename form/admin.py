from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Jogo, Juiz, Time

class JogoResource(resources.ModelResource):
    class Meta:
        model = Jogo

@admin.register(Jogo)
class JogoAdmin(ImportExportModelAdmin):
    resource_class = JogoResource
    
admin.site.register(Juiz)
admin.site.register(Time)


admin.site.site_header = "Análise Esportiva Admin"