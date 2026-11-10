from django import forms
from django.core.exceptions import ValidationError
from .models import SolicitudAuditoria
import os


class SolicitudAuditoriaForm(forms.ModelForm):
    class Meta:
        model = SolicitudAuditoria
        fields = ['nombre', 'unidad_responsable', 'fecha_inicio_encargo',
                  'fecha_final_encargo', 'solicitud_especial', 'nombramiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'unidad_responsable': forms.TextInput(attrs={'placeholder': 'Unidad responsable'}),
            'fecha_inicio_encargo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_final_encargo': forms.DateInput(attrs={'type': 'date'}),
            'solicitud_especial': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Solicitud especial (opcional)'}),
            'nombramiento': forms.FileInput(attrs={'accept': '.pdf,.jpg,.jpeg'}),
        }

    def clean_nombramiento(self):
        f = self.cleaned_data.get('nombramiento')
        if f:
            ext = os.path.splitext(f.name)[1].lower()
            if ext not in ['.pdf', '.jpg', '.jpeg']:
                raise ValidationError('Solo se permiten archivos PDF o JPG.')
            if f.size > 5 * 1024 * 1024:
                raise ValidationError('El archivo no debe superar 5 MB.')
        return f

    def clean(self):
        cleaned = super().clean()
        fi = cleaned.get('fecha_inicio_encargo')
        ff = cleaned.get('fecha_final_encargo')
        if fi and ff and ff < fi:
            raise ValidationError('La fecha final no puede ser anterior a la fecha de inicio.')
        return cleaned