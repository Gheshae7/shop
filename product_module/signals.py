from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Product, ManyImages, Category, Brand
from pathlib import Path
import os


@receiver(post_delete, sender=Product)
def delete_image_on_product(sender, instance, **kwargs):
    if instance.image:
        path = Path(instance.image.path)
        if path.is_file():
            path.unlink()


@receiver(pre_save, sender=Product)
def delete_image_product_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_product = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return
    if current_product.image != instance.image:
        if current_product.image and os.path.isfile(current_product.image.path):
            os.remove(current_product.image.path)


@receiver(post_delete, sender=ManyImages)
def delete_image_on_many_image(sender, instance, **kwargs):
    if instance.image:
        path = Path(instance.image.path)
        if path.is_file():
            path.unlink()


@receiver(pre_save, sender=ManyImages)
def delete_image_many_image_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_many_image = ManyImages.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return
    if current_many_image.image != instance.image:
        if current_many_image.image and os.path.isfile(current_many_image.image.path):
            os.remove(current_many_image.image.path)


@receiver(post_delete, sender=Brand)
def delete_image_on_brand(sender, instance, **kwargs):
    if instance.image:
        path = Path(instance.image.path)
        if path.is_file():
            path.unlink()


@receiver(pre_save, sender=Brand)
def delete_image_brand_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_brand = Brand.objects.get(pk=instance.pk)
    except Brand.DoesNotExist:
        return
    if current_brand.image != instance.image:
        if current_brand.image and os.path.isfile(current_brand.image.path):
            os.remove(current_brand.image.path)


@receiver(post_delete, sender=Category)
def delete_image_on_brand(sender, instance, **kwargs):
    if instance.image:
        path = Path(instance.image.path)
        if path.is_file():
            path.unlink()


@receiver(pre_save, sender=Category)
def delete_image_brand_on_modify(sender, instance, **kwargs):
    if not instance.pk:
        pass
    try:
        current_category = Category.objects.get(pk=instance.pk)
    except Category.DoesNotExist:
        return
    if current_category.image != instance.image:
        if current_category.image and os.path.isfile(current_category.image.path):
            os.remove(current_category.image.path)
