from django.shortcuts import render


def formVenta(request):
    return render(request,'form_venta.html')