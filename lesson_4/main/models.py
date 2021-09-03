from django.db import models


class Goods(models.Model):
    UNIT_PRICE = {
        ('RUB', 'руб.'),
        ('USD', '$'),
        ('EUR', 'euro')
    }
    published_date = models.DateField(verbose_name='дата публикации товара', auto_now_add=True)
    name = models.CharField(verbose_name='название товара', max_length=128)
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=2)
    unit_price = models.CharField(verbose_name='ед. цены', choices=UNIT_PRICE, default='руб.', max_length=64)
    supplier = models.CharField(verbose_name='имя поставщика', max_length=128)

    class Meta:
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

