from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {"content": "留言內容"}
        widgets = {
            "content": Textarea(
                attrs={
                    "class": "textarea",
                    "rows": 5,
                }
            ),
        }
