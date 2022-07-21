from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    locality=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES, max_length=240)

    def __str__(self):
        return self.name

category_choices=(
    ('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'),
)

class Product(models.Model):
    title=models.CharField(max_length=250)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=250)
    category=models.CharField(choices=category_choices, max_length=10)
    product_image=models.FileField(upload_to='productimg')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product

status_choices=(
    ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=status_choices, max_length=250, default='Pending')

    def __str__(self):
        return self.product