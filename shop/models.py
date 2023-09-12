from django.db import models

class Product(models.Model):
    pid = models.AutoField 
    name = models.CharField(max_length=63)
    price = models.IntegerField(default=-1)
    desc = models.CharField(max_length=255)
    datePublished = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    category = models.CharField(max_length=64, default="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=63)
    email = models.CharField(max_length=63)
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    