from django.urls import path
from .views import list,producto_por_id, agregar_proveedor, agregar_producto, editar_producto, eliminar_producto, editar_proveedor, eliminar_proveedor

app_name = 'compra'

urlpatterns = [
    path('', list, name='list'),
    path('<int:id>/', producto_por_id, name='producto_por_id'),
    path('agregar_proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('editar_proveedor/<int:id>/', editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:id>/', eliminar_proveedor, name='eliminar_proveedor'),
]