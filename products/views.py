from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductCreateForm, RawProductCreateForm, ProductDeleteForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    
    context = {
        'object': obj
    }
    return render(request, "products/products_detail.html", context)

def product_create_view(request):
    initial_data = {
        'title': "New product Title",
        'description': "New Product Description"
    }
    form = ProductCreateForm(request.POST or None,initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        'form': form
    }

    return render(request, "products/products_create.html", context)

def product_edit_view(request, product_id):
    # obj = Product.objects.get(id=product_id)
    obj = get_object_or_404(Product,id=product_id)
    form = ProductCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        'form': form
    }

    return render(request, "products/products_create.html", context)

def product_delete_view(request, product_id):
    obj = get_object_or_404(Product,id=product_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = {
        'object': obj
    }

    return render(request, "products/products_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/products_list.html", context)