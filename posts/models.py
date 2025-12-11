from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(max_length=144)
    slug = models.SlugField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    banner = models.ImageField(blank=True, upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title # No changes to DB with function, no need for migration
    

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)