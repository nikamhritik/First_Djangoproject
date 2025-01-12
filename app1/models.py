from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_joined = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    def __repr__(self):
        return str(self)
    
    class Meta:
        db_table = "product"
