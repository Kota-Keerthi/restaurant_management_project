from django.shortcuts import render, redirect
from .models import ContactMessageForm
# Create your views here.

def home(request):
    if request.merhod == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()        
    return render(request, 'home.html', {'form': form})
    })
