from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.list import ListView


from mainapp.models import Product, ProductCategory

def index(request):
    context = {
        'head': 'geekShop - главная',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, category_id=None):
    menu_names = ProductCategory.objects.all()
    page = request.GET.get('page', 1)

    if not category_id:
        category_name= ''
        cards = Product.objects.all()
    else:
        category_name = ProductCategory.objects.get(id=category_id)
        cards = Product.objects.filter(category=category_name)
    products_on_page = 2
    paginator = Paginator(cards, products_on_page)
    # page_obj = paginator.get_page(page) рекомендуется исп для классов,
    # page если нет нужной страницы - ошибка, get_page ошибки нет
    context = {
        'head': 'geekShop - каталог',
        'menu_names': menu_names,
        # 'cards': cards,
        # 'page_obj': page_obj, рекомендуется
        'cards': paginator.page(page),
        'category_name': category_name,
    }
    return render(request, 'mainapp/products.html', context)





