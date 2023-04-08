from django.db import models

class Position(models.Model):
    name = models.CharField("Должность", max_length=120)
    is_active = models.BooleanField("Активна?", default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
    
