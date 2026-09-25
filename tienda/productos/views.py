from django.shortcuts import render
from .models import Producto


def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/listado.html", {"productos": productos})


def registrar_producto(request):
    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST["nombre"],
            categoria=request.POST["categoria"],
            precio=request.POST["precio"],
            cantidad=request.POST["cantidad"]
        )
        return render(request, "productos/listado.html", {"productos": Producto.objects.all()})
    return render(request, "productos/form.html")