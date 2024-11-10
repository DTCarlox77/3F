from django.db import models

# Create your models here.
class Fruta(models.Model):
    
    nombre = models.CharField(max_length=50, null=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return f'Fruta: {self.nombre}'