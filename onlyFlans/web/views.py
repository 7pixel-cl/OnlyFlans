from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Flan
from .forms import ContactFormModelForm

def home(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {'flanes': flanes})

def bienvenido(request):
    flanes = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {'flanes': flanes})

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
