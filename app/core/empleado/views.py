from django.shortcuts import render


def formEmpleado(request):
    return render(request,'form_empleado.html')