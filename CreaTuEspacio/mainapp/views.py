from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm , InsertarUsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import usuariosCentro

# Create your views here.

def index(request):
    return render ( request , 'mainapp/index.html', {
        'title' : 'Inicio'
    })

def inicio_usuarios(request):
    return render (request , 'mainapp/inicio.html',{
        'title' : 'Inicio'
    } )


def about(request):
    return render ( request , 'mainapp/about.html', {
        'title' : 'Sobre nosotros'
    })

def register_page(request):
    
    if request.user.is_authenticated:
        return redirect('inicio_usuarios')
    else: 

     register_form = RegisterForm()

    if request.method == 'POST':
      
       register_form = RegisterForm(request.POST)

       if register_form.is_valid():
           register_form.save()
           messages.success(request, 'Te haz registrado correctamente')

           return redirect('inicio_usuarios')

    return render(request , 'users/register.html' , {
        'title' : 'Registro',
        'register_form': register_form
    })


def login_page(request):
    

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username = username , password = password)

        if user is not None:
            login(request , user)
            return redirect('inicio_usuarios')
        
        else:
            messages.warning(request, 'No te haz identificado correctamente')


    return render(request , 'users/login.html' , {
        'title' : 'Iniciar sesión'
    })


def logout_user(request):

    logout(request)
    return redirect('login')

def insertar_usuarios_centro(request):
    if request.method == 'POST':
        form = InsertarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lista_usuarios')  
    else:
        form = InsertarUsuarioForm()

    data = {'form': form}
    return render(request, 'mainapp/usuarios.html', data)
   
   


   
def listar_usuarios_centro(request):
    usuarios = usuariosCentro.objects.all()
    data = {'usuarios' : usuarios}
    return render(request , 'mainapp/listaUsuarios.html' , data)
                  

def eliminar_usuario(request, id):
    usuario = usuariosCentro.objects.get(id = id)
    usuario.delete()
    return redirect('lista_usuarios')


def actualizar_usuario(request, id):
    usuario = usuariosCentro.objects.get(id = id)
    form = InsertarUsuarioForm(instance = usuario)
    if request.method == 'POST' :
        form = InsertarUsuarioForm(request.POST , instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('lista_usuarios')
    data = {'form' : form}
    return render(request , 'mainapp/usuarios.html' , data)