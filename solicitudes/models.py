from django.db import models
from django.contrib.auth.models import User


ESTADOS = [
    ('pendiente', 'Pendiente'),
    ('en_proceso', 'En proceso'),
    ('atendida', 'Atendida'),
    ('rechazada', 'Rechazada'),
]


class SolicitudAuditoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes')
    nombre = models.CharField('Nombre del funcionario', max_length=200)
    unidad_responsable = models.CharField('Unidad responsable', max_length=200)
    fecha_inicio_encargo = models.DateField('Fecha inicio de encargo')
    fecha_final_encargo = models.DateField('Fecha final de encargo')
    solicitud_especial = models.TextField('Solicitud especial', blank=True)
    nombramiento = models.FileField('Nombramiento (PDF/JPG)', upload_to='nombramientos/%Y/%m/')
    estado = models.CharField('Estado', max_length=20, choices=ESTADOS, default='pendiente')
    observaciones_admin = models.TextField('Observaciones del administrador', blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creado_en']
        verbose_name = 'Solicitud de auditoría'
        verbose_name_plural = 'Solicitudes de auditoría'

    def __str__(self):
        return f'{self.nombre} - {self.unidad_responsable} ({self.get_estado_display()})'