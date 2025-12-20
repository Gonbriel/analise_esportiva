from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import AnalysisModel

@admin.register(AnalysisModel)
class AnalysisModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ver_dashboard')

    def ver_dashboard(self, obj):
        if obj.dashboard_html:
            url = reverse(
                'dashboard',
                args=[obj.dashboard_html.name]
            )
            return format_html(
                '<a href="{}" target="_blank">Ver dashboard</a>',
                url
            )
        return '-'

    ver_dashboard.short_description = 'Dashboard'