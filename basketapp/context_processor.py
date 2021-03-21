from basketapp.models import Basket


def basket(request):
    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)
        if user_basket:
            total_sum = sum(basket.sum() for basket in user_basket)
            total_quantity = sum(basket.quantity for basket in user_basket)
            return {'basket': f'В корзине {total_quantity} товаров на сумму {total_sum} руб.', }
        return {'basket': 'Корзина пуста'}

    return {'basket': ''}



