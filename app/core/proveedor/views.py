from django.shortcuts import render


def formProveedor(request):
    return render(request,'form_proveedor.html')

def formVisitador(request):
    return render(request,'form_visitador.html')