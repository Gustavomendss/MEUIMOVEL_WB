from django.db import models

# CRIANDO O  MODELO PARA O MEUIMOVEL

class todo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)

class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class MEUIMOVELapp(Base):
    título = models.CharField(max_length=255)
    url = models.URLField(unique=True)


    class Meta:
        verbose_name = 'MEUIMOVEL'
        verbose_name_plural = 'MEUIMOVEL'


    def __str__(self):
        return self.título

# Criando a parte de avaliacao
class Avaliacao(Base):
    MEUIMOVEL = models.ForeignKey(MEUIMOVELapp,
                               related_name='avaliacoes',
                               on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email','MEUIMOVEL']

        def __str__(self):
            return f'{self.nome} avaliou o MEUIMOVEL {self.MEUIMOVEL} com a nota {self.avaliacao}'

