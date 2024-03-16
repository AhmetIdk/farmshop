from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CommentForm, SearchForm
from django.contrib import messages

from product.models import *
from home.models import *

# Create your views here.
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(title__icontains=query)
            context = {"urunler": results}
            return render(request,'shop.html', context)
    return HttpResponseRedirect('/')

def shop(request):
    urunler = Product.objects.order_by('?')[:6]
    context = {"urunler": urunler}
    return render(request,'shop.html', context)

def productDetail(request, id, slug):
    urun = Product.objects.get(id=id)
    urunler= Product.objects.filter(category_id=urun.category_id)
    images = Image.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id)
    
    context = {"urun": urun, "images": images, "urunler":urunler, "comments":comments}
    return render(request, 'shop-detail.html', context)

def addComment(request, id):
    url = request.META.get('HTTP_REFERER')  # geldiğimiz sayfanın url bilgisini verir
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            current_user = request.user
            data.user_id = current_user.id
            data.product_id = id
            data.save()
            messages.success(request, "yorumunuz başarıyla kaydedildi")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)