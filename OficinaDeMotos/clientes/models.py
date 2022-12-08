from django.db import models

class clientes(models.Model):

    id_clientes = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    CPF = models.CharField(max_length=11)

    def __str__(self):
        return self.nome