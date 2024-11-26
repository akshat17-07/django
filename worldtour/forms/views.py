from django.shortcuts import render, redirect

# Create your views here.
from .forms import ContactForm

def home_view(request):
    return render(request, 'form/home.html')

def contact_view (request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
        
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'form/contact.html', context)
    
def contact_success_view(request):
    return render(request, 'form/contact_success.html')