from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html',)
    elif request.method == "POST":
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        pessoa = Pessoa(nome=nome,idade=idade)
        pessoa.save()
        return HttpResponse("Pessoa cadastrada com sucesso")
