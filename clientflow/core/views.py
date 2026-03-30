from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm


def home(request):
    return render(request, 'core/home.html')

@login_required
def clientes_list(request):
    clientes = Cliente.objects.filter(user=request.user)
    return render(request, 'core/clientes_list.html', {'clientes': clientes})


@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()

    return render(request, 'core/cliente_form.html', {'form': form})

@login_required
def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, id=id, user=request.user)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'core/cliente_form.html', {'form': form})

@login_required
def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id, user=request.user)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_list')

    return render(request, 'core/cliente_confirm_delete.html', {'cliente': cliente})

