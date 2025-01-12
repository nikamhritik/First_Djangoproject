
import datetime
from django.db.models import Avg
from django.db.models import Count
from app1.models import Product

#exec(open(r'C:\Users\hritik\Documents\Hritik\Django Framework\first_project\Assignment\app1\db-shell.py').read())

# all_products = Product.objects.all()
# print(all_products)

# pro = Product.objects.filter(price__gte = 10000)
# print(pro)

# for i in all_products:
#     print(i)

# for i in all_products:
#     print(i.__dict__)

# try:
#     pro = Product.objects.get(id=4)
#     print(pro)
# except:
#     print("Employee with given ID doesn't exist")


#CRUD Operations
# 1st Way
# prod = Product(name="Printer", brand="HP", price=29000, quantity=12)

# prod.save()

# 2nd Way
# Product.objects.create(name="Scanner", brand="Inkjet", price=17000, quantity=8)

# Update
# try:
#     pro_obj = Product.objects.get(id=1)
#     pro_obj.brand = "Inkjet"
# except Product.DoesNotExist:
#     print("Product with given ID doesn't exist")

# Delete
# try:
#     pro_obj = Product.objects.get(id=1)
#     pro_obj.delete()
# except Product.DoesNotExist:
#     print("Product with given ID doesn't exist")

# Filter

# pro = Product.objects.filter(brand = "Inkjet")
# print(pro)

# pro = Product.objects.filter(brand__startswith = "H")
# print(pro)

# avg_price = Product.objects.aggregate(Avg("price"))
# print(avg_price)
# prod_count = Product.objects.filter(brand = "HP").aggregate(Count('id'))
# print(prod_count)

top_2_expensive_prod = Product.objects.order_by("-price")[:2]
print(top_2_expensive_prod)