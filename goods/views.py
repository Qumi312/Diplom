from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.models import Categories, Products


def catalog(request, category_slug):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    context = {"title": "Home - Каталог", "goods": goods}
    return render(request, "goods/catalog.html", context)


def product(request, product_slug=False, product_id=False):

    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)
    context = {"product": product}
    return render(request, "goods/product.html", context)
