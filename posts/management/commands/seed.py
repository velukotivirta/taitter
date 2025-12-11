import os
import shutil
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.get(username="admin")
        static_path = os.path.join(settings.BASE_DIR, "static", "images", "mush.jpg")
        media_path = os.path.join(settings.MEDIA_ROOT, "mush.jpg")
        shutil.copy(static_path, media_path)
        object = {"title": "Sieni.", "body": "Sieniä on."}
        for i in range(100):
            post = Post.objects.create(
                title=object["title"],
                body=object["body"],
                author=user,
                date=timezone.now() + timedelta(days=i)
            )
            with open(media_path, "rb") as f:
                post.banner.save(f"mush.jpg", File(f), save=True)
        self.stdout.write(self.style.SUCCESS("100 post objektia luotu."))