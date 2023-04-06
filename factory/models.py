from django.db import models

# Create your models here.


class Order(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name='Клиент',
        on_delete=models.)
    name_order = models.ForeignKey(
        ProductModel,
        verbose_name='Модель',
        on_delete=models.CASCADE)
    data_poluchenia = models.DateField(
        auto_now_add=True, verbose_name='Дата Получения')
    quantity_zayav = models.IntegerField(
        default=0, verbose_name='Количество Заявленное')
    quantity_fact = models.IntegerField(
        default=0, verbose_name='Количество Фактически выполненного')
    data_zakup = models.DateField(auto_now=True, verbose_name='Дата закупа')
    raskroi_tkani = models.DateField(verbose_name='Дата когда раскроили')
    pod_flizelin = models.DateField(verbose_name='Дата подклейки флизелина')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'Имя клиента {self.client}. Имя продутка {self.name_order}.'
