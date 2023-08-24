from django.db import models

# Create your models here.
class produc(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    price = models.FloatField(verbose_name='precio')
    stock = models.PositiveBigIntegerField(verbose_name='cantidad')
    color = models.CharField(max_length=10, verbose_name='color')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'producto'
        ordering = ['id']
        verbose_name = 'Producto'
        verbose_name_plural = 'productos'
class prueba_modulo(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    questions = models.PositiveIntegerField(verbose_name='preguntas')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'prueba'
        ordering = ['id']
        verbose_name = 'prueba'
        verbose_name_plural = 'prueba'
        
    