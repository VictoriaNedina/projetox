from django.db import models

# Create your models here.
class Crush(models.Model):
    signo_opcoes = [
        ('Áries', 'áries'),
        ('Touro', 'touro'),
        ('Gêmeos', 'gêmeos'),
        ('Câncer', 'câncer'),
        ('Leão', 'leão'),
        ('Virgem', 'virgem'),
        ('Libra', 'libra'),
        ('Escorpião', 'escorpião'),
        ('Sagitário', 'sagitário'),
        ('Capricórnio', 'capricornio'),
        ('Aquário', 'aquário'),
        ('Peixes', 'peixes')
    ]

    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100, default='não está comigo')
    signo = models.CharField(max_length=20, choices=signo_opcoes)
    reciproco = models.BooleanField(default=False)
    solteiro = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.nome