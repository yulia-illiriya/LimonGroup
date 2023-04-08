from django.db import models

class Price(models.Model):
    created_at = models.DateTimeField("Запись создана", auto_now_add=True)
    updated_at = models.DateTimeField("Запись обновлена", auto_now=True)
    start_date = models.DateTimeField("Цена действительна с")
    end_date = models.DateTimeField("Цена действительна до")
    is_actual = models.BooleanField("Актуально?", default=True)
    value = models.DecimalField("Стоимость")
    
    def __str__(self): 
        return self.value
    
    class Meta:
        verbose_name = "Стоимость пошива"
        verbose_name = "Цены"
        ordering = ['updated_at']
