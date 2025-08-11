from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import CommentForm
from articles.models import Article
from django.contrib import messages
from django.views.decorators.http import require_POST, require_http_methods
from .models import Comment


@require_POST
def create(request, id):
    article = get_object_or_404(Article, pk=id)

    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.article = article
    comment.save()

    return render(request, "comments/comment.html", {"comment": comment})


@require_http_methods(["DELETE"])
def delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()

    return HttpResponse("")
