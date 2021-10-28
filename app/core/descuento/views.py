from django.shortcuts import render


def formDescuento(request):
    return render(request,'form_descuento.html')