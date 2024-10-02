from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.
def login(request):
    return render(request, 'login.html')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senhas não coincidem.')
            return redirect('/usuarios/cadastro')
        
        if len(senha) <6:
            messages.add_message(request, constants.ERROR, 'A senha deve conter pelo menos 6 digítos.')
            return redirect('/usuarios/cadastro')
        
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome.')
            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        return redirect ('/usuarios/login')
    
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, email=email, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/home/buy')

        messages.add_message(request, constants.ERROR, 'Email ou senha inválidos')
        return redirect('/usuarios/login')

    
