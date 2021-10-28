from django.shortcuts import render


def formProducto(request):
    return render(request,'form_producto.html')