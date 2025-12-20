from django.db import models

class AnalysisModel(models.Model):
    nome = models.CharField(max_length=100)
    dashboard_html = models.FileField(
        upload_to='dashboards/',
        null=False,
        blank=False
    )