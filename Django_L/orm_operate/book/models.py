from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return '{},{},{}'.format(self.name, self.author, self.price)
