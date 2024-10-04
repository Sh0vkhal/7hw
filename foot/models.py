from django.db import models

# Create your models here.


class Retsept(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    food = models.ForeignKey(Retsept, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
   

    def __str__(self) -> str:
        return self.name
    

class Deliver(models.Model):
    food = models.ForeignKey(Retsept, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.food
