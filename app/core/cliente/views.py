from django.shortcuts import render

# Create your views here.
def formCliente(request):
    return render(request,'form_cliente.html')