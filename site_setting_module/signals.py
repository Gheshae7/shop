from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import SettingSite, Baner
import os


@receiver(post_delete, sender=SettingSite)
def delete_logo_on_site_setting(sender, instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)
            
            
            
@receiver(pre_save, sender=SettingSite)
def delete_logo_sitesetting_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_site_setting = SettingSite.objects.get(pk=instance.pk)
    except SettingSite.DoesNotExist:
        return
    if current_site_setting.logo != instance.logo:
        if current_site_setting.logo and os.path.isfile(current_site_setting.logo.path):
            os.remove(current_site_setting.logo.path)




@receiver(post_delete, sender=Baner)
def delete_image_on_baner(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            
            
            
@receiver(pre_save, sender=Baner)
def delete_image_baner_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_baner = Baner.objects.get(pk=instance.pk)
    except Baner.DoesNotExist:
        return
    if current_baner.image != instance.image:
        if current_baner.image and os.path.isfile(current_baner.image.path):
            os.remove(current_baner.image.path)