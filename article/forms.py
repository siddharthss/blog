from django import forms


class CreateArticle(forms.Form):
    title = forms.CharField(max_length=100)
    creator = forms.CharField(max_length=100)
    pub_date = forms.DateField()
    content = forms.Textarea()
