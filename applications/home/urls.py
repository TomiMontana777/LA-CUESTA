#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('panel/', views.PanelHomeView.as_view(), name='panel-home'),
    path(
        'admin/', 
        views.PanelAdminView.as_view(),
        name='index-admin',
    ),
    path(
        'admin-reporte/', 
        views.ReporteAdmin.as_view(),
        name='admin-reporte',
    ),
    path(
        'admin-liquidacion/', 
        views.ReporteLiquidacion.as_view(),
        name='admin-liquidacion',
    ),
    path(
        'admin-resumen-ventas/', 
        views.ReporteResumenVentas.as_view(),
        name='admin-resumen_ventas',
    ),
]