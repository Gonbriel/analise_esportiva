from django.db import models

CAMPEONATOS = sorted((
    ('Brasileiro: Série A', 'Brasileiro: Série A'),
    ('Brasileiro: Série B', 'Brasileiro: Série B'),
    ('Premier League', 'Premier League'),
    ('La Liga', 'La Liga'),
    ('Bundesliga', 'Bundesliga'),
    ('Italiano: Serie A', 'Italiano: Serie A'),
    ('Ligue 1', 'Ligue 1'),
))

class Time(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
    
class Juiz(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        db_table = 'juizes'
        verbose_name = 'Juiz'
        verbose_name_plural = 'Juízes'

class Jogo(models.Model):
    campeonato = models.CharField(max_length=50, choices=CAMPEONATOS)
    rodada = models.IntegerField()
    data = models.DateField()
    mandante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogos_mandante')
    visitante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogos_visitante')
    resultado = models.CharField(
    max_length=1,
    choices=[('M', 'Mandante'), ('V', 'Visitante'), ('E', 'Empate')],
    null=True, blank=True
)
    gols_mandante = models.IntegerField()
    gols_visitante = models.IntegerField()
    faltas_mandante = models.IntegerField(null=True, blank=True)
    faltas_visitante = models.IntegerField(null=True, blank=True)
    cartoes_mandante = models.IntegerField(null=True, blank=True)
    cartoes_visitante = models.IntegerField(null=True, blank=True)
    escanteios_mandante = models.IntegerField(null=True, blank=True)
    escanteios_visitante = models.IntegerField(null=True, blank=True)
    posse_bola_mandante = models.FloatField(null=True, blank=True)
    posse_bola_visitante = models.FloatField(null=True, blank=True)
    publico = models.IntegerField(null=True, blank=True)
    chutes_mandante = models.IntegerField(null=True, blank=True)
    chutes_visitante = models.IntegerField(null=True, blank=True)
    juiz = models.ForeignKey(Juiz, on_delete=models.SET_NULL, null=True, blank=True)
    
    def save(self, *args, **kwargs):
            if self.gols_mandante > self.gols_visitante:
                self.resultado = 'M'
            elif self.gols_mandante < self.gols_visitante:
                self.resultado = 'V'
            else:
                self.resultado = 'E'
            super().save(*args, **kwargs)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['campeonato', 'data', 'mandante', 'visitante'],
                name='unique_jogo'
            )
        ]

    
    def __str__(self):
        return f"{self.mandante} vs {self.visitante} - {self.campeonato} on {self.data}"