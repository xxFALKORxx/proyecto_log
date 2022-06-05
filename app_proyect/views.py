from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from app_proyect.models import Products
from app_proyect.forms import Product_form

def products(request):
        productos = Products.objects.all()
        context = {'productos':productos}
        return render(request, 'products.html', context=context)

def create_product(request):
	if request.method == 'GET':
		form = Product_form()
		context = {'form':form}
		return render(request, 'create_product.html', context = context)
	else:
		form = Product_form(request.POST)
		if form.is_valid():
			new_product = Products.objects.create(
				name = form.cleaned_data['name'],
				price = form.cleaned_data['price'],
				description = form.cleaned_data['description'],
				SKU = form.cleaned_data['SKU'],
				active = form.cleaned_data['active'],
				)
			context = {'new_product':new_product}
		return render(request, 'create_product.html', context = context)

def search_product_view(request):
	print(request.GET)
	product_search = Products.objects.filter(name__icontains = request.GET['search'])
	context = {'product_search':product_search}
	return render (request, 'search_product.html', context = context)