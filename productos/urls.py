from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_producto>/', views.ver_producto, name='ver_producto'),
    path('agregar/', views.agregar, name='agregar'),
    path('editar/<int:id_producto>/', views.editar, name='editar'),
    path('eliminar/<int:id_producto>/', views.eliminar, name='eliminar'),
]
