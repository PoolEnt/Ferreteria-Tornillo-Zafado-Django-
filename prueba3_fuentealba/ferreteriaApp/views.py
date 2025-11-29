from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto
from .forms import ProductoForm
# Create your views here.



def es_administrador(user):
    return user.username == 'administrador'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales Incorrectas'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    es_admin = request.user.username == 'administrador'
    return render(request, 'index.html', {'es_admin': es_admin})

@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    es_admin = request.user.username == 'administrador'
    return render(request, 'listar.html', {'productos': productos, 'es_admin': es_admin})

@login_required
def buscar_producto(request):
    productos = []
    busqueda = ''
    es_admin = request.user.username == 'administrador'
    
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda', '')
        if busqueda: 
            productos = Producto.objects.filter(nombre__icontains=busqueda)
    
    return render(request, 'buscar_producto.html', {
        'productos': productos, 
        'busqueda': busqueda,
        'es_admin': es_admin
    })

@login_required
@user_passes_test(es_administrador)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def modificar_producto(request, id):
    producto = Producto(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
    else:
        fecha_formateada = ''
        if producto.fecha_ingreso:
            fecha_formateada = producto.fecha_ingreso.strftime('%d/%m/%y')
        
        initial_data = {
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'stock': producto.stock,
            'precio_unitario': producto.precio_unitario,
            'fecha_ingreso': fecha_formateada,
            'categoria': producto.categoria,
        }
        form = ProductoForm(initial=initial_data, instance=producto)
    
    return render(request, 'modificar_producto.html', {'form': form, 'producto': producto})

@login_required
@user_passes_test(es_administrador)
def eliminar_producto(request, id=id):
    producto = Producto(id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_producto')
    return render(request, 'eliminar_producto.html', {'producto': producto})