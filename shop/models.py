from django.db import models

# Create your models here.
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

