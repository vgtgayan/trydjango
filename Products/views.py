from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
def product_create_view(request):
    # Renders the form if POST is true. Otherwise render out empty form.
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # form.save(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    """ context = {
        'name': obj.name,
        'description': obj.description
    } """
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)

def single_product_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    """ context = {
        'name': obj.name,
        'description': obj.description
    } """
    context = {
        'objects': obj
    }
    return render(request, 'products/product_details.html', context)

def delete_product_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'objects': obj
    }    
    return render(request, 'products/product_delete.html', context)