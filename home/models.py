from django.db import models
from django.conf import settings


class Search(models.Model):
    tag = models.CharField(max_length=300)
    counter = models.PositiveIntegerField(default=0)
    search_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag