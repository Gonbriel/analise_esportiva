from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Jogo, Juiz, Time


class JogoResource(resources.ModelResource):
    mandante = fields.Field(
        column_name='Mandante',
        attribute='mandante',
        widget=ForeignKeyWidget(Time, 'nome')
    )

    visitante = fields.Field(
        column_name='Visitante',
        attribute='visitante',
        widget=ForeignKeyWidget(Time, 'nome')
    )
    juiz = fields.Field(
        column_name='Juiz',
        attribute='juiz',
        widget=ForeignKeyWidget(Juiz, 'nome')
    )

    class Meta:
        model = Jogo
        exclude = ('id',)

@admin.register(Jogo)
class JogoAdmin(ImportExportModelAdmin):
    resource_class = JogoResource
    
admin.site.register(Juiz)
admin.site.register(Time)

admin.site.site_header = "PSI - Performance & Sports Intelligence"