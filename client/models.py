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

