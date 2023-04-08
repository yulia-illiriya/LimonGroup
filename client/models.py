from django.db import models


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
