from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from home.models import Tag


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name) if not new_slug else new_slug
    queryset = Tag.objects.filter(slug=slug).exclude(id=instance.id)
    if queryset.exists():
        slug = f"{slug}-{queryset.count() + 1}"
    return slug


@receiver(pre_save, sender=Tag)
def pre_save_slugify(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
