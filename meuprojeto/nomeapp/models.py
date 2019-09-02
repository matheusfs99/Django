from django.db import models

class Aluno(models.Model):

    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    genero = models.CharField(max_length=30)

    def __str__(self):
        return '{} - Nome: {} | Idade: {} | Gênero: {}'.format(self.id, self.nome, self.idade, self.genero)