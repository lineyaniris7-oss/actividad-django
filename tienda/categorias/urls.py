from django.urls import path
from . import views

urlpatterns = [

    path("", views.registrar_categorias),

    path("lista_categorias/", views.lista_categorias),

    path("detalle_categorias/<int:id>/", views.detalle_categorias),

    path("editar_categorias/<int:id>/", views.editar_categorias),

    path("eliminar_categorias/<int:id>/", views.eliminar_categorias),

]
