from django.shortcuts import render, get_object_or_404
from  django.http import HttpResponse
from catalog.models import Product


def home(request):
    flowers = Product.objects.all()
    context = {"products": flowers}
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо {name}! Ваше сообщение получено.')
    return render(request, 'contacts.html')

def one_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'one_product.html', context)
