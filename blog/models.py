from django.db import models
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')

    def __str__(self):
        return self.title
