from django.shortcuts import render
from .models import usuarios as ModelUsuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = ModelUsuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    dados_usuarios = {
        'usuarios': ModelUsuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', dados_usuarios)