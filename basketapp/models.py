from functools import cached_property
from django.db import models

from authapp.models import User
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @cached_property
    def basket_for_user(self):
        return Basket.objects.filter(user=self.user)

    def total_quantity(self):
        baskets = self.basket_for_user
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = self.basket_for_user
        return sum(basket.sum() for basket in baskets)

    objects = BasketQuerySet.as_manager()

    def save(self, *args, **kwargs):
        quantity = self.product.quantity
        if self.pk:
            self.product.quantity -= self.quantity - Basket.objects.get(pk=self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        if self.product.quantity < 0:
            self.product.quantity = quantity
            return f'товар {self.product.name} закончился'
        self.product.save()
        super(Basket, self).save(*args, **kwargs)
