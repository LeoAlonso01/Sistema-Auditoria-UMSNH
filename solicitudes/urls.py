from django.urls import path
from . import views

urlpatterns = [
    path('nueva/', views.nueva_solicitud, name='nueva_solicitud'),
    path('mis/', views.mis_solicitudes, name='mis_solicitudes'),
    path('<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('<int:pk>/pdf/', views.generar_pdf, name='generar_pdf'),
]