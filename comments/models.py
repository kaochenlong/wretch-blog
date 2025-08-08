from django.db import models
from articles.models import Article


class Comment(models.Model):
    content = models.TextField(null=False)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, db_index=True)
