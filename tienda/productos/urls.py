from django.urls import path
from . import views

urlpatterns = [

    path("", views.registrar_productos),

    path("listado_productos/", views.listado_productos),

    path("detalle_productos/<int:id>/", views.detalle_productos),

    path("editar_productos/<int:id>/", views.editar_productos),

    path("eliminar_productos/<int:id>/", views.eliminar_productos),

]
