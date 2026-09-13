from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import User
import os


@receiver(post_delete, sender=User)
def delete_image_on_user(sender, instance, **kwargs):
    if instance.avatra:
        if os.path.isfile(instance.avatra.path):
            os.remove(instance.avatra.path)


@receiver(pre_save, sender=User)
def delete_avatar_user_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return
    if current_user.avatra != instance.avatra:
        if current_user.avatra and os.path.isfile(current_user.avatra.path):
            os.remove(current_user.avatra.path)
