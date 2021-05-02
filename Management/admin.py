from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin

# Register your models here.



admin.site.register(Works_in)

admin.site.register(MakesFood)
admin.site.register(Maintains_by)
admin.site.register(Use)
admin.site.register(Inventory)


@admin.register(Staff,Customer,Menu,Staff_phoneNo,Customer_phoneNo,Order,Reservation,Shift,Order_Menu,PlaceOrder,Delivery,Makes_Delievery,Transaction)
class ViewAdmin(ImportExportModelAdmin):
    # exclude = ('id', )
    pass


