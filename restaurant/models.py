from unicodedata import category
from django.db import models


# Create your models here.

class Category(models.Model):
    cname=models.TextField(max_length=20,primary_key=True)
    torders=models.IntegerField()
    def __str__(self):
        return self.cname

class FoodItem(models.Model):
    name=models.TextField(max_length=40)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField(max_length=100,default="its juicy")
    pimage=models.ImageField(upload_to="restaurant/images",default="")
    price=models.IntegerField()
    profitPerUnit=models.IntegerField()
    totalOrders=models.IntegerField()
    rating=models.FloatField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_firstname=models.CharField(max_length=12,default="xyz")
    order_lastname=models.CharField(max_length=12,default="karki")
    order_username=models.CharField(max_length=20,default="")
    order_id=models.IntegerField(default=0)
    order_contact1=models.CharField(max_length=20,default="")
    order_contact2=models.CharField(max_length=20,default="")
    order_email=models.CharField(max_length=20,default="")
    order_location=models.CharField(max_length=30,default="")
    order_allorders=models.CharField(max_length=200,default="")
    order_track=models.CharField(max_length=20,default="onprocess")
 
    def __str__(self):
        # return (self.order_firstname)
        if self.order_track == "onprocess":
            return (self.order_firstname)
        else:
            return (self.order_track)
        


class Review(models.Model):
    username=models.TextField(max_length=20)
    review=models.TextField(max_length=300)

    def __str__(self):
        return self.username


class SpecialItem(models.Model):
    name=models.TextField(max_length=40)
    category=models.TextField(max_length=40)
    # category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField(max_length=100,default="its juicy")
    pimage=models.ImageField(upload_to="restaurant/images",default="")
    price=models.IntegerField()
    rating=models.FloatField()

    def __str__(self):
        return self.name