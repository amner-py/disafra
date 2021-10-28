from django.shortcuts import render


def formPago(request):
    return render(request,'form_pago.html')