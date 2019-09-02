from django.shortcuts import render, redirect
from.models import Aluno
from .forms import AlunoForm

def listar(request):
    context = {}
    alunos = Aluno.objects.all()
    context['alunos'] = alunos

    return render(request, 'listar.html', context)

def buscar(request, id):
    context = {}
    try:
        aluno = Aluno.objects.get(id=id)
        context ['aluno'] = aluno
    except Exception as e:
        context ['aluno'] = 'Aluno não encontrado!'
    return render(request, 'buscar.html', context)

def remover(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {'aluno': aluno}
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar')
    return render(request, 'confirmar-remover.html', context)

def cadastrar(request):
    form = AlunoForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'cadastrar.html', context)

def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'editar.html', context)