from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Veg_item)
admin.site.register(Non_veg_item)
admin.site.register(Menu)
admin.site.register(Neutral)