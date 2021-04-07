from django.db import models
from django.conf import settings
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PROCEED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SEND_TO_PROCEED, 'отправлен в обработку'),
        (PROCEED, 'обрабатывается'),
        (PAID, 'оплачен',),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменён'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлён', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created',)

    def __str__(self):
        return 'Текущий заказ: {}'.format(self.id)

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum((list(map(lambda x: x.quantity * x.product.price, items))))

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()

    def get_summary(self):
        items = self.orderitems.select_related()
        total_cost = sum(list(map(lambda x: x.get_product_cost(), items)))
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return {
            'total_cost': total_cost,
            'total_quantity':total_quantity,
        }


class OrderItemQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(OrderItemQuerySet, self).delete()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='колличество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    object = OrderItemQuerySet.as_manager()

    def save(self, *args, **kwargs):
        quantity = self.product.quantity
        if self.pk:
            self.product.quantity -= self.quantity - OrderItem.objects.get(pk=self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        if self.product.quantity < 0:
            self.product.quantity = quantity
            return f'не дхватает товара {self.product.name}. На складе только {self.product.quantity}шт.'
        self.product.save()
        super(OrderItem, self).save(*args, **kwargs)
