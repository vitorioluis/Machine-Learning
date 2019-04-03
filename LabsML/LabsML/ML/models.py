from django.db import models

n, b, d = 10, False, None


# Create your models here.

class Iris(models.Model):
    SepalLengthCm = models.DecimalField('Compr. da Sépala', blank=b, default=d, max_digits=n, decimal_places=2, )
    SepalWidthCm = models.DecimalField('Largura da Sépala', blank=b, default=d, max_digits=n, decimal_places=2)
    PetalLengthCm = models.DecimalField('Compr. da Petula', blank=b, default=d, max_digits=n, decimal_places=2)
    PetalWidthCm = models.DecimalField('Largura da Petula', blank=b, default=d, max_digits=n, decimal_places=2)
    Species = models.CharField('Espécie', blank=True, max_length=30, default=None)

    def __str__(self):
        return self.Species

    class Meta:
        db_table = 'tb_ml_iris'
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"


class Acoes(models.Model):
    data = models.CharField('Data', blank=True, max_length=10, default=None)
    open = models.DecimalField('Valor na Abertura', blank=b, default=d, max_digits=n, decimal_places=4)
    max = models.DecimalField('Valor Máximo', blank=b, default=d, max_digits=n, decimal_places=4)
    min = models.DecimalField('Valor Mínimo', blank=b, default=d, max_digits=n, decimal_places=4)
    close = models.DecimalField('Valor do Fechamento', blank=b, default=d, max_digits=n, decimal_places=4)
    adj_close = models.DecimalField('Valor Ajustado no Fechamento', blank=b, default=d, max_digits=n, decimal_places=4)
    volume = models.IntegerField('Volume de Transações', blank=b, default=d)

    def __str__(self):
        return str(self.volume)

    class Meta:
        db_table = "tb_ml_acoes"
        verbose_name = "Regresão Linear"


class Filmes(models.Model):

    ano_lançamento = models.CharField('Ano Lançamento', blank=True, max_length=10, default=None)
    titulo_obra = models.CharField('Título', blank=True, max_length=200, default=None)
    genero = models.CharField('Gêneto', blank=True, max_length=50, default=None)
    pais_produtor_obra = models.CharField('País Produtor da Obra', blank=True, max_length=100, default=None)
    nacionalidade_obra = models.CharField('Nacionalidade', blank=True, max_length=100, default=None)
    data_lançamento = models.CharField('Data Lançamento', blank=True, max_length=10, default=None)
    distribuidora = models.CharField('Distribuidora', blank=True, max_length=200, default=None)
    salas_lançamento = models.IntegerField('Salas de Lançamento', blank=b, default=d)
    maximo_salas_ocupadas = models.IntegerField('Mámo de salas Ocupadas', blank=b, default=d)
    publico_acumulado = models.IntegerField('Publico Acumulado', blank=b, default=d)
    renda_acumulada = models.FloatField('Renda Acumulada', blank=b, default=d)

    def __str__(self):
        return self.titulo_obra

    class Meta:
        db_table="tb_ml_filmes"
        verbose_name = "Sistema de Recomendação"
