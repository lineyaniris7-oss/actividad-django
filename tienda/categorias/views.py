from django.shortcuts import render
from .models import Categoria


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/lista.html", {"categorias": categorias})


def registrar_categorias(request):
    if request.method == "POST":
        Categoria.objects.create(
            nombre=request.POST["nombre"],
            observaciones=request.POST["observaciones"]
        )
        return render(request, "categorias/lista.html", {"categorias": Categoria.objects.all()})
    return render(request, "categorias/formulario.html")

def detalle_categorias(request, id):

    categoria = Categoria.objects.get(id=id)

    return render(
        request,
        "categorias/detalles.html",
        {"categoria": categoria}
    )

def editar_categorias(request, id):

    categoria = Categoria.objects.get(id=id)

    if request.method == "POST":

        categoria.nombre = request.POST["nombre"]
        categoria.observaciones = request.POST["observaciones"]

        categoria.save()

        return render(
            request,
            "categorias/detalles.html",
            {"categoria": categoria}
        )

    return render(
        request,
        "categorias/formulario.html",
        {"categoria": categoria}
    )

def eliminar_categorias(request, id):

    categoria = Categoria.objects.get(id=id)

    categoria.delete()

    return render(
        request,
        "categorias/lista.html",
        {"categorias": Categoria.objects.all()}
    )
