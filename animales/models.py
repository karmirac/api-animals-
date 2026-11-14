from django.db import models


class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre