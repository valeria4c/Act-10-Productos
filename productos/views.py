from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import producto
from .forms import ProductoForm

# Lista todos los productos
def index(request):
    return render(request, 'productos/index.html', {
        'productos': producto.objects.all()
    })

# Ver un producto
def ver_producto(request, id_producto):
    product = get_object_or_404(producto, pk=id_producto)
    return render(request, 'productos/ver_producto.html', {'producto': product})

# Agregar un producto
def agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'productos/agregar.html', {'form': ProductoForm(), 'success': True})
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar.html', {'form': form, 'success': False})

# Editar un producto existente
def editar(request, id_producto):
    product = get_object_or_404(producto, pk=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'productos/editar.html', {'form': form, 'success': True})
    else:
        form = ProductoForm(instance=product)
    return render(request, 'productos/editar.html', {'form': form, 'success': False})

# Eliminar un producto
def eliminar(request, id_producto):
    product = get_object_or_404(producto, pk=id_producto)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'productos/eliminar.html', {'producto': product})
