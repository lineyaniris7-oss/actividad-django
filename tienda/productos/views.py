from django.shortcuts import render
from .models import Producto


def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/listado.html", {"productos": productos})


def registrar_productos(request):
    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST["nombre"],
            categoria=request.POST["categoria"],
            precio=request.POST["precio"],
            cantidad=request.POST["cantidad"]
        )
        return render(request, "productos/listado.html", {"productos": Producto.objects.all()})
    return render(request, "productos/form.html")

def detalle_productos(request, id):

    producto = Producto.objects.get(id=id)

    return render(
        request,
        "productos/detalle.html",
        {"producto": producto}
    )

def editar_productos(request, id):

    producto = Producto.objects.get(id=id)

    if request.method == "POST":

        producto.nombre = request.POST["nombre"]
        producto.categoria = request.POST["categoria"]
        producto.precio = request.POST["precio"]
        producto.cantidad = request.POST["cantidad"]
        producto.estado = request.POST.get("estado") == "True"

        producto.save()

        return render(
            request,
            "productos/detalle.html",
            {"producto": producto}
        )

    return render(
        request,
        "productos/form.html",
        {"producto": producto}
    )

def eliminar_productos(request, id):

    producto = Producto.objects.get(id=id)

    producto.delete()

    return render(
        request,
        "productos/listado.html",
        {"productos": Producto.objects.all()}
    )