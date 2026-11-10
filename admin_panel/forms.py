from django import forms
from solicitudes.models import SolicitudAuditoria
from .models import FormatoOficio


class SolicitudAdminForm(forms.ModelForm):
    class Meta:
        model = SolicitudAuditoria
        fields = ['nombre', 'unidad_responsable', 'fecha_inicio_encargo',
                  'fecha_final_encargo', 'solicitud_especial', 'estado',
                  'observaciones_admin', 'nombramiento']
        widgets = {
            'nombre': forms.TextInput(),
            'unidad_responsable': forms.TextInput(),
            'fecha_inicio_encargo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_final_encargo': forms.DateInput(attrs={'type': 'date'}),
            'solicitud_especial': forms.Textarea(attrs={'rows': 4}),
            'observaciones_admin': forms.Textarea(attrs={'rows': 4}),
            'nombramiento': forms.FileInput(attrs={'accept': '.pdf,.jpg,.jpeg'}),
        }


class FormatoOficioForm(forms.ModelForm):
    class Meta:
        model = FormatoOficio
        fields = ['nombre', 'plantilla_html', 'activo']
        widgets = {
            'nombre': forms.TextInput(),
            'plantilla_html': forms.Textarea(attrs={'rows': 20, 'style': 'font-family:monospace'}),
            'activo': forms.CheckboxInput(),
        }