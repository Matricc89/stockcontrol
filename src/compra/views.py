from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

# Create your views here.

def list(request):
    lista_productos = Producto.objects.all()
    return render(request,'compra/list.html',{'lista_productos': lista_productos})

def producto_por_id(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'compra/producto_id.html', {'producto': producto})


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra:list')
    else:
        form = ProveedorForm()
    return render(request, 'compra/proveedor_form.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra:list')
    else:
        form = ProductoForm()
    return render(request, 'compra/producto_form.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('compra:list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'compra/producto_form.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('compra:list')
    return render(request, 'compra/confirmar_eliminar_producto.html', {'producto': producto})

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('compra:list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'compra/proveedor_form.html', {'form': form})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('compra:list')
    return render(request,  {'proveedor': proveedor})