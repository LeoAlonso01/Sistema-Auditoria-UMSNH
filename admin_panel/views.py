from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from fpdf import FPDF
from solicitudes.models import SolicitudAuditoria
from .models import FormatoOficio
from .forms import SolicitudAdminForm, FormatoOficioForm


def es_admin(u):
    return u.is_authenticated and u.is_staff


@login_required
@user_passes_test(es_admin)
def dashboard_admin(request):
    total = SolicitudAuditoria.objects.count()
    pendientes = SolicitudAuditoria.objects.filter(estado='pendiente').count()
    return render(request, 'admin_panel/dashboard.html', {'total': total, 'pendientes': pendientes})


@login_required
@user_passes_test(es_admin)
def listado_solicitudes(request):
    qs = SolicitudAuditoria.objects.all()
    estado = request.GET.get('estado')
    if estado:
        qs = qs.filter(estado=estado)
    return render(request, 'admin_panel/listado.html', {'solicitudes': qs, 'estado': estado})


@login_required
@user_passes_test(es_admin)
def detalle_admin(request, pk):
    s = get_object_or_404(SolicitudAuditoria, pk=pk)
    return render(request, 'admin_panel/detalle.html', {'solicitud': s})


@login_required
@user_passes_test(es_admin)
def editar_solicitud(request, pk):
    s = get_object_or_404(SolicitudAuditoria, pk=pk)
    if request.method == 'POST':
        form = SolicitudAdminForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud actualizada.')
            return redirect('detalle_admin', pk=s.pk)
    else:
        form = SolicitudAdminForm(instance=s)
    return render(request, 'admin_panel/editar.html', {'form': form, 'solicitud': s})


@login_required
@user_passes_test(es_admin)
def generar_pdf_admin(request, pk):
    s = get_object_or_404(SolicitudAuditoria, pk=pk)
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
    pdf.cell(0, 8, f'Observaciones: {s.observaciones_admin or "-"}', ln=True)
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, 'Solicitud especial:', ln=True)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 8, s.solicitud_especial or 'Sin solicitud especial.')
    content = bytes(pdf.output(dest='S'))
    resp = HttpResponse(content, content_type='application/pdf')
    resp['Content-Disposition'] = f'attachment; filename="solicitud_{s.pk}.pdf"'
    return resp


@login_required
@user_passes_test(es_admin)
def listado_formatos(request):
    qs = FormatoOficio.objects.all()
    return render(request, 'admin_panel/formatos.html', {'formatos': qs})


@login_required
@user_passes_test(es_admin)
def editar_formato(request, pk):
    f = get_object_or_404(FormatoOficio, pk=pk)
    if request.method == 'POST':
        form = FormatoOficioForm(request.POST, instance=f)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formato actualizado.')
            return redirect('listado_formatos')
    else:
        form = FormatoOficioForm(instance=f)
    return render(request, 'admin_panel/editar_formato.html', {'form': form, 'formato': f})


@login_required
@user_passes_test(es_admin)
def nuevo_formato(request):
    if request.method == 'POST':
        form = FormatoOficioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formato creado.')
            return redirect('listado_formatos')
    else:
        form = FormatoOficioForm()
    return render(request, 'admin_panel/nuevo_formato.html', {'form': form})