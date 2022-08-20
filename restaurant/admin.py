from django.contrib import admin
from .models import FoodItem,Orders,Category,Review,SpecialItem

# Register your models here.

admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Orders)
admin.site.register(Review)
admin.site.register(SpecialItem)

