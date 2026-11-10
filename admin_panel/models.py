from django.db import models
from django.contrib.auth.models import User


class FormatoOficio(models.Model):
    nombre = models.CharField('Nombre del formato', max_length=100)
    plantilla_html = models.TextField('Plantilla HTML')
    activo = models.BooleanField('Activo', default=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-actualizado_en']
        verbose_name = 'Formato de oficio'
        verbose_name_plural = 'Formatos de oficio'

    def __str__(self):
        return self.nombre