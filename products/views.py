from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def create_raw_product(request):
    my_form = RawProductForm()

    if request.method == "POST":
        my_form = RawProductForm(request.POST)

        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        'form': my_form
    }
    return render(request, "products/create.html", context)

def create_simple_product(request):
    if request.method == "POST":
        print(request.POST.get("title"))
        # Product.objects.create(title=request.POST.get("title"))

    return render(request, "products/raw_create.html", {})

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form
    }
    return render(request, "products/create.html", context)

def get_product(request, *args, **kwargs):
    obj = Product.objects.get(id=1)

    context = {
        'object': obj
    }

    return render(request, "products/details.html", context)

def dynamic_product_view(request, id):
    # obj = Product.objects.get(id=id)

    obj = get_object_or_404(Product, id=id)

    context = {
        "object": obj
    }

    return render(request, "products/details.html", context)


def delete_product_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')

    context = {
        'object': obj
    }
    return render(request, 'products/delete.html', context)

def get_products(request):
    object_list = Product.objects.all()

    context = {
        'object_list': object_list
    }

    return render(request, 'products/list.html', context)