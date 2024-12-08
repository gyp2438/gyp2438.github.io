from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from blog.models import Post


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title) if not new_slug else new_slug
    queryset = Post.objects.filter(slug=slug).exclude(id=instance.id)
    if queryset.exists():
        slug = f"{slug}-{queryset.count() + 1}"
    return slug


@receiver(pre_save, sender=Post)
def pre_save_slugify(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
