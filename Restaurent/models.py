from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    position=models.IntegerField()


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    menu_category = models.CharField(max_length=20)
    item_type = models.CharField(max_length=2)

class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through=OrderItem) 
    created_at = models.DateTimeField(auto_now_add=True)
    Amount=models.IntegerField(default=0)


