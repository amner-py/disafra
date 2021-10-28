from django.shortcuts import render

# Create your views here.
def formCompra(request):
    return render(request,'form_compra.html')