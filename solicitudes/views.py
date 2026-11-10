import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from fpdf import FPDF
from .models import SolicitudAuditoria
from .forms import SolicitudAuditoriaForm


@login_required
def nueva_solicitud(request):
    if request.method == 'POST':
        form = SolicitudAuditoriaForm(request.POST, request.FILES)
        if form.is_valid():
            s = form.save(commit=False)
            s.usuario = request.user
            s.save()
            messages.success(request, 'Solicitud creada correctamente.')
            return redirect('mis_solicitudes')
    else:
        form = SolicitudAuditoriaForm()
    return render(request, 'solicitudes/nueva.html', {'form': form})


@login_required
def mis_solicitudes(request):
    qs = SolicitudAuditoria.objects.filter(usuario=request.user)
    return render(request, 'solicitudes/mis.html', {'solicitudes': qs})


@login_required
def detalle_solicitud(request, pk):
    s = get_object_or_404(SolicitudAuditoria, pk=pk, usuario=request.user)
    return render(request, 'solicitudes/detalle.html', {'solicitud': s})


def _generar_pdf_solicitud(s):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'OFICIO DE SOLICITUD DE AUDITORIA', ln=True, align='C')
    pdf.set_font('Helvetica', '', 11)
    pdf.ln(5)
    pdf.cell(0, 8, f'Nombre: {s.nombre}', ln=True)
    pdf.cell(0, 8, f'Unidad responsable: {s.unidad_responsable}', ln=True)
    pdf.cell(0, 8, f'Fecha inicio de encargo: {s.fecha_inicio_encargo}', ln=True)
    pdf.cell(0, 8, f'Fecha final de encargo: {s.fecha_final_encargo}', ln=True)
    pdf.cell(0, 8, f'Estado: {s.get_estado_display()}', ln=True)
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, 'Solicitud especial:', ln=True)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 8, s.solicitud_especial or 'Sin solicitud especial.')
    pdf.ln(5)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.cell(0, 8, f'Generado: {s.creado_en.strftime("%d/%m/%Y %H:%M")}', ln=True)
    return bytes(pdf.output(dest='S'))


@login_required
def generar_pdf(request, pk):
    s = get_object_or_404(SolicitudAuditoria, pk=pk, usuario=request.user)
    content = _generar_pdf_solicitud(s)
    resp = HttpResponse(content, content_type='application/pdf')
    resp['Content-Disposition'] = f'attachment; filename="solicitud_{s.pk}.pdf"'
    return resp