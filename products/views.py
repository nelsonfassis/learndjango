from django.shortcuts import render
from .models import Product
from .forms import ProductCreateForm, RawProductCreateForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    
    context = {
        'object': obj
    }
    return render(request, "products/products_detail.html", context)

def product_create_view(request):
    form = RawProductCreateForm()
    if request.method == "POST":
        form = RawProductCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = ProductCreateForm()
        else:
            print(form.errors)
                
    context = {
        "form": form
    }
    return render(request, "products/products_create.html", context)

# def product_create_view(request):
#     form = ProductCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()

#     context = {
#         'form': form
#     }

#     return render(request, "products/products_create.html", context)
