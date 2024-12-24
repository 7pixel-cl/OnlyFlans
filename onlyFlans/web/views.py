from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flan
from .forms import ContactFormModelForm

def home(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {'flanes': flanes})

@login_required
def bienvenido(request):
    flanes = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {'flanes': flanes})

def detalle_flan(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    # Si el flan es privado, verificar que el usuario esté autenticado
    if flan.is_private and not request.user.is_authenticated:
        messages.error(request, 'Necesitas iniciar sesión para ver este flan exclusivo.')
        return redirect('login')
    return render(request, "flan_detail.html", {'flan': flan})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarnos! Te responderemos pronto.')
            return redirect('exito')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ContactFormModelForm()
    return render(request, "contact.html", {'form': form})

def exito(request):
    return render(request, "success.html")

def acerca(request):
    return render(request, "about.html")
