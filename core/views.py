from datetime import datetime
from django.http.response import Http404

from django.shortcuts import render
from django.shortcuts import redirect
from django.core.cache import cache
from django.urls.base import reverse
from django.views.defaults import page_not_found

from .forms import CreateProductForm
from .forms import FindProductForm
from core.search.sequential import seq
from .utils import append_product_to_file
from .utils import is_exist
from .utils import count_file
from .utils import search_by_position

# Create your views here.


def index(request):
    form = FindProductForm()
    form_create = CreateProductForm()
    return render(request, 'core/index.html', {'form': form, 'form_create': form_create})


def search_no_indexed(request):
    if request.method == 'POST':
        form = FindProductForm(request.POST)
        if form.is_valid():
            product_id = str(form.cleaned_data['product_id'])

            # Start algorithm
            start_time = datetime.now()

            try:
                product = seq(product_id)
                product[0]
            except Exception:
                return page_not_found(request, 'core/404.html')

            end_time = datetime.now()

            # Calculated total time
            total_time = end_time - start_time
            total_time = total_time.total_seconds() * 1000

            # Data to render
            data = {
                'title': 'Busqueda No Indexada',
                'product_id': product[0],
                'price': product[1],
                'position': product[2],
                'time': total_time
            }
            print(data)
            return render(request, 'core/result.html', {'data': data})
    return redirect(index)


def search_indexed(request):
    if request.method == 'POST':
        form = FindProductForm(request.POST)
        if form.is_valid():
            bplustree = cache.get('bplustree')
            product_id = str(form.cleaned_data['product_id'])
            
            # Start algorithm
            start_time = datetime.now()
            
            try:
                position = bplustree.retrieve(product_id)
                product = search_by_position(position)
                product[0]
            except Exception:
                return page_not_found(request, 'core/404.html')

            end_time = datetime.now()

            # Calculated total time
            total_time = end_time - start_time
            total_time = total_time.total_seconds() * 1000

            # Data to render
            data = {
                'title': 'Busqueda Indexada',
                'product_id': product[0],
                'price': product[1],
                'position': product[2],
                'time': total_time
            }
            print(data)
            return render(request, 'core/result.html', {'data': data})
    return redirect(index)


def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            # Get values
            product_id = str(form.cleaned_data['product_id'])
            price = str(form.cleaned_data['price'])

            if not is_exist(product_id):
                bplustree = cache.get('bplustree')
                
                count = count_file() + 1
                
                bplustree.insert(product_id, count)
                bplustree.show()

                # Append product to file
                append_product_to_file(product_id, price)
            else:
                print('Producto no creado')
                return page_not_found(request, 'core/404.html')
    return redirect(index)