from django.db import models

# Create your models here.
class Veg_item(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    menu_category=models.CharField(max_length=20)
class Non_veg_item(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    menu_category=models.CharField(max_length=20)
class Menu(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    position=models.IntegerField()
class Neutral(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    menu_category=models.CharField(max_length=20)