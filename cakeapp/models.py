from django.db import models

# Create your models here.
class cake_intro(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='picture')


class about(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='picture')

class items(models.Model):
    name = models.CharField(max_length=100)

class orange(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    price = models.IntegerField()
    desc = models.TextField(max_length=250)


class blueberry(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')

class banana(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')

class apple(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')

class mango(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')

class strawberry(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')

class customer_say(models.Model):
    head = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    name = models.CharField(max_length=100)
    desc = models.TextField()



