# from django.db.models.signals import post_save, pre_delete
#
# from django.dispatch import receiver
# from .models import QuantityModel
#
#
# @receiver(post_save, sender=QuantityModel)
# def my_callback(sender, instance, **kwargs):
#     daily_work = instance.daily_work
#     daily_work.total_cost += (instance.sewing_model.client_price.value * instance.quantity)
#     daily_work.daily_salary = daily_work.total_cost - daily_work.prepayment
#     daily_work.save()
#     print(instance)
#
#
# @receiver(pre_delete, sender=QuantityModel)
# def my_callback2(sender, instance, **kwargs):
#     daily_work = instance.daily_work
#     daily_work.total_cost -= (instance.sewing_model.client_price.value * instance.quantity)
#     daily_work.daily_salary = daily_work.total_cost - daily_work.prepayment
#     daily_work.save()
#     print(instance)
