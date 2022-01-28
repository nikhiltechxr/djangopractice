from itertools import product
from django.contrib import admin
from .models import ProductTable, CategoryTable

# Register your models here.

admin.site.register(ProductTable)
admin.site.register(CategoryTable)

'''@admin.register(ProductTable)
class ProductTableAdmin(admin.ModelAdmin):
    list_display=[ 'ProductTable.prod_name' , 'ProductTable.pro_detail']
'''

