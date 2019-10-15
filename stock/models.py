from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    department = models.CharField(max_length=100, default='')
    sub_department = models.CharField(max_length=100, default='')
    stockLevel = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
   

    def __str__(self):
        return self.name
