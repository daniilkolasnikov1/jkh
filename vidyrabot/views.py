from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm


def vidyrabot_home(request):
    vidyrabot = Artiles.objects.all()
    return render(request, 'vidyrabot/vidyrabot_home.html', {'vidyrabot':vidyrabot})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()

    data = {
        'form': form,
        'error' : error
    }

    return render(request, 'vidyrabot/create.html', data)
