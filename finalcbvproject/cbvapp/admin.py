from django.contrib import admin
from cbvapp.models import Beer
# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display = ['name','price','flavour','food_mate','country']
admin.site.register(Beer,BeerAdmin)
