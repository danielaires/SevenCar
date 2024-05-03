from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login


#Exibir as Informações
def registro(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = Usuario(name=name, email=email, senha=senha)
        usuario.save()
        return redirect('home')
    return render(request, 'registro.html')

def login_cadastro(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = authenticate(request, email=email, senha=senha)
        if usuario is not None:
            login(request, usuario) 
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Email ou senha invalidos'})
    return render(request, 'login.html')

   

    

