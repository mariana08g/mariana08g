from django.db import models
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from datetime import datetime 

class kitty(models.Model):
    id = models.PositiveIntegerField(verbose_name='id', primary_key=True, null=False)
    nombre = models.CharField(max_length=50, verbose_name='nombre')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = 'kitty' 
        verbose_name_plural = 'kitty'
        db_table = 'kitty' 
        ordering = ['id'] 
            