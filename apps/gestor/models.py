from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length= 200)
    nascimento = models.DateField(verbose_name='Nascimento')
    cpf = models.CharField(verbose_name='CPF', max_length= 14) #000.000.000-00

    def __str__(self):
        return self.nome

class Conta(models.Model):
    TIPO_CONTA_CHOICE = (
        ('RB', 'A receber'),
        ('PG', 'A pagar'),
    )
    pessoa = models.ForeignKey(Pessoa, verbose_name='Pessoa', on_delete=models.CASCADE)
    tipo_conta = models.CharField(verbose_name='Tipo de Conta', max_length=2, choices=TIPO_CONTA_CHOICE)
    vencimento = models.DateField(verbose_name='vencimento')
    valor = models.DecimalField(verbose_name='valor R$', max_digits=19, decimal_places=2)

    def __str__(self):
        return "Nome: {} - Valor R$: {}".format(self.pessoa.nome, self.valor)

