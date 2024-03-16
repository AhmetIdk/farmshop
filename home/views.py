from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from product.models import *
from .forms import *

# Create your views here.
def index(request):
    categories = Category.objects.order_by('?')[:3]
    context = {"categories": categories}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # print(form.cleaned_data['name'])
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('contact')

    form = ContactForm
    context = {"page":"İletişim","form":ContactForm}
    return render(request, 'contact.html',context)

def gallery(request):
    gallery = GalleryImage.objects.order_by('?')[:6]
    context = {"gallery": gallery}
    return render(request, 'gallery.html', context)

