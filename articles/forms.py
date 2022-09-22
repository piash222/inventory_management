from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already in use")


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # only clean the title so cleaned data only contains title
    def clean_title(self):
        cleaned_data = self.cleaned_data  # dictionary
        print('cleaned_data', cleaned_data)
        title = cleaned_data.get('title')
        # if title.lower().strip() == "the article":
        #     raise forms.ValidationError("This title is taken")
        # print('title', title)
        return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        title = cleaned_data.get('title')
        if title.lower().strip() == "the article":
            self.add_error('title', "This title is taken")

        content = cleaned_data.get('content')
        if "office" in content:
            self.add_error('content', "office cant be in content")

        print('title', title)
        return self.cleaned_data
