from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=False)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
