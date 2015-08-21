from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    content = models.TextField()
    user_fk = models.ForeignKey(User)





