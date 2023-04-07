from django.db import models
from employees import Employee
from client import Client

# Create your models here.


class Order(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name='Клиент',
        on_delete=models.CASCADE)
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


class DailyWork(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Cотрудник")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Модель")  # модель
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    prepayment = models.IntegerField(default=0, verbose_name="Аванс")

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "Ежедневник"
        verbose_name_plural = "Ежедневники"


class NewOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Модель")
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=25)
    image = models.ImageField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    received_date = models.DateField(verbose_name="Дата получения")
    delivery_date = models.DateField(verbose_name="Дата отправки")

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = "Образец"
        verbose_name_plural = "Образцы"
