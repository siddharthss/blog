from django import forms


class RegisterUserTest(forms.Form):
    name = forms.CharField(label="your name", max_length=10)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class CreateUser(forms.Form):
    name = forms.CharField(label=" name", max_length=100)
    username = forms.CharField(label="user name", max_length=100)
    password = forms.CharField(label="password", max_length=100)
    repassword = forms.CharField(label="re-enter  password", max_length=100)
