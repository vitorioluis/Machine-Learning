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


class tb_ml_preco_combustivel(models.Model):
    uf = models.CharField('UF', blank=True, max_length=5, default=None)
    municipio = models.CharField('Município', blank=True, max_length=100, default=None)
    data = models.CharField('Data', blank=True, max_length=10, default=None)
    posto = models.CharField('Posto', blank=True, max_length=100, default=None)
    bandeira = models.CharField('Bandeira', blank=True, max_length=50, default=None)
    produto = models.CharField('produto', blank=True, max_length=20, default=None)
    preco = models.DecimalField('Preço', blank=b, default=d, max_digits=n, decimal_places=4)

    def __str__(self):
        return self.posto

    class Meta:
        db_table = "tb_ml_preco_combustível"
        verbose_name = "Preços Combustiveis"
        verbose_name_plural = "Preço Combustível"
