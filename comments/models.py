from django.db import models
from articles.models import Article
from datetime import datetime
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField(null=False)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, db_index=True)

    def delete(self):
        self.deleted_at = datetime.now()
        self.save()
