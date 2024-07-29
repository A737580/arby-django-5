from django.contrib import admin

from .models import Product


admin.site.site_header = "My Django app"
admin.site.site_title = "Title of Django app"
admin.site.index_title = "My admin site"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','description')
    search_fields = ('name',)  #Это обязательно картежи
    list_editable = ('price', 'description')
    actions = ('make_zero',)

    def make_zero(self,request,queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)

