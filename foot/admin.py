from django.contrib import admin

# Register your models here.
from .models import Retsept,Product,Deliver

admin.site.register(Retsept)
admin.site.register(Product)
admin.site.register(Deliver)
