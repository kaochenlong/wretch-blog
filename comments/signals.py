from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Comment


@receiver(post_save, sender=Comment)
def created_or_deleted(sender, instance, created, **kwags):
    username = instance.user.username

    if created:
        print(f"{username} 新增了一則留言")
    else:
        print(f"{username}，你的留言被刪了！")
