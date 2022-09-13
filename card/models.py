from django.db import models

# Create your models here.

class Africa(models.Model):

    country = models.CharField(max_length=50)

    capital = models.CharField(max_length=50)

    def __str__(self):

        return str(self.country)


class Human(models.Model):

    name = models.CharField(max_length=50)

    sex = models.CharField(choices=(('male','Male'),('female','Female')),max_length=40)

    age = models.PositiveIntegerField(default=0)

    def __str__(self):

        return str(self.name)
