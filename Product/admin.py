from django.contrib import admin
from Product.models import Product, Category, Methods, SuitableCompany, UseCases, DataAttribute, Frequency, Format, \
    Volume, Pricing, Provider

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Methods)
admin.site.register(SuitableCompany)
admin.site.register(UseCases)
admin.site.register(DataAttribute)
admin.site.register(Frequency)
admin.site.register(Format)
admin.site.register(Volume)
admin.site.register(Pricing)
admin.site.register(Provider)
