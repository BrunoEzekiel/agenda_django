from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="Email")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('contato_detail', kwargs={'pk': self.pk})
