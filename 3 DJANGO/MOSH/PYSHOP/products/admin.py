from django.contrib import admin
from .models import Product,Offer


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock']           # these attributes display in the admin panel area

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','offer')


admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)



