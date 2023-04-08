from django.db import models

class Client(models.Model):
    full_name = models.CharField("Полное имя", max_length=120)
    contacts = models.CharField("Контакты", max_length=200)
    address = models.CharField("Адрес", max_length=200)
    is_new = models.BooleanField("Новый клиент", default=True)
    created_at = models.DateTimeField("Запись создана", auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['full_name']



class CatalogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Каталог Категория:')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка:')

    class Meta:
        verbose_name = 'Категория Каталога'
        verbose_name_plural = 'Категория Каталогов'

    def __str__(self):
        return self.name


class Catalog(models.Model):
    articul = models.CharField(max_length=200, verbose_name='Артикуль:')
    colors = models.CharField(max_length=100, verbose_name='Цвет:')
    size = models.IntegerField(default=0, verbose_name='Размер:')
    image = models.ImageField(
        upload_to='media/%Y/%m/%d',
        verbose_name='Изображение:')
    quantity = models.IntegerField(default=0, verbose_name='Количество:')
    category = models.ForeignKey(
        CatalogCategory,
        verbose_name='Категория:',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return f"Артикул: {self.articul} Количество: {self.quantity} Категория: {self.category}"
