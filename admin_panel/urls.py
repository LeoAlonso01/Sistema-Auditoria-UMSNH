from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_admin, name='dashboard_admin'),
    path('solicitudes/', views.listado_solicitudes, name='listado_solicitudes'),
    path('solicitudes/<int:pk>/', views.detalle_admin, name='detalle_admin'),
    path('solicitudes/<int:pk>/editar/', views.editar_solicitud, name='editar_solicitud'),
    path('solicitudes/<int:pk>/pdf/', views.generar_pdf_admin, name='generar_pdf_admin'),
    path('formatos/', views.listado_formatos, name='listado_formatos'),
    path('formatos/<int:pk>/editar/', views.editar_formato, name='editar_formato'),
    path('formatos/nuevo/', views.nuevo_formato, name='nuevo_formato'),
]