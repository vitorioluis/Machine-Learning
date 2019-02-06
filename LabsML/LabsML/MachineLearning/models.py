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


class tb_ml_acoes(models.Model):
    data = models.CharField('Data', blank=True, max_length=10, default=None)
    open = models.DecimalField('Abertura', blank=b, default=d, max_digits=n, decimal_places=4)
    max = models.DecimalField('Valor Máximo', blank=b, default=d, max_digits=n, decimal_places=4)
    min = models.DecimalField('Valor Mínimo', blank=b, default=d, max_digits=n, decimal_places=4)
    close = models.DecimalField('Valor do Fechamento', blank=b, default=d, max_digits=n, decimal_places=4)
    adj_close = models.DecimalField('Preço Ajustado Fechamento', blank=b, default=d, max_digits=n, decimal_places=4)
    volume = models.IntegerField('Volume de Transações', blank=b, default=d)

    def __str__(self):
        return str(self.volume)

    class Meta:
        db_table = "tb_ml_acoes"
        verbose_name = "Regresão Linear"
