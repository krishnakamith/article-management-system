from django import forms
from .models import Article

ARTICLE_STATUS = (
            ("draft", "draft"),
            ("inprogress", "in progress"),
            ("published", "published"),
        )

class CreateArticleForms(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    twitter_post =  forms.CharField(widget=forms.Textarea, required=False)
    status = forms.ChoiceField(choices = ARTICLE_STATUS)
