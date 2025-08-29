from django.shortcuts import render, redirect
from .models import ContactMessageForm
from .forms import ContactForm
# Create your views here.

def contact_view(request):
    if request.merhod == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
    
            return HttpResponse("<h3>Thank you for contacting us!</h3>")
    else:
        form = ContactForm()        
    return render(request, "contact.html", {'form': form})
    })
