from django.shortcuts import render

def inicio(request):
    return render(request, 'web_landing/inicio.html')

def servicios(request):
    return render(request, 'web_landing/servicios.html')

def precios(request):
    return render(request, 'web_landing/precios.html')

def clientes(request):
    return render(request, 'web_landing/clientes.html')

def contacto(request):
    return render(request, 'web_landing/contacto.html')
