from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse


def home(request):
    category = Catgory.objects.filter(sub_cat=False)
    return render(request, 'home/home.html', {'category': category})


def all_product(request, slug=None, id=None):
    category = Catgory.objects.filter(sub_cat=False)
    products = Product.objects.all()
    if slug and id:
        data = get_object_or_404(Catgory, slug=slug, id=id)
        products = products.filter(category=data)

    return render(request, 'home/product.html', {'products': products, 'category': category})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    if product.status != 'None':
        if request.method == 'POST':
            variant = Vareiants.objects.filter(product_variant_id=id)
            var_id= request.POST.get('select')
            variants = Vareiants.objects.get(id=var_id)
        else:
            variant = Vareiants.objects.filter(product_variant_id=id)
            variants = Vareiants.objects.get(id=variant[0].id)
        context = {'product':product,'variant':variant}
        return render(request, 'home/detail.html',)
    else:
        return render(request,'home/detail.html',{'product':product})