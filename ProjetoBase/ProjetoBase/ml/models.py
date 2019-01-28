from django.db import models


# Create your models here.

class Iris(models.Model):
    n, b, d = 10, False, None

    SepalLengthCm = models.DecimalField('Compr. da Sépala', blank=b, default=d, max_digits=n, decimal_places=2,)
    SepalWidthCm = models.DecimalField('Largura da Sépala', blank=b, default=d, max_digits=n, decimal_places=2)
    PetalLengthCm = models.DecimalField('Compr. da Petula', blank=b, default=d, max_digits=n, decimal_places=2)
    PetalWidthCm = models.DecimalField('Largura da Petula', blank=b, default=d, max_digits=n, decimal_places=2)
    Species = models.CharField('Espécie', blank=True, max_length=30, default=None)

    def __str__(self):
        return self.Species

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"
