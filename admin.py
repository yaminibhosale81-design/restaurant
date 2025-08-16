from django.contrib import admin
from Restro.models import Booking,Online_Order,Cancel_Order,Cancel_Booking,Userlogin,Adminlogin,register
admin.site.register(Booking)
admin.site.register(Online_Order)
admin.site.register(Cancel_Order)
admin.site.register(Cancel_Booking)
admin.site.register(Userlogin)
admin.site.register(Adminlogin)
admin.site.register(register)
# Register your models here.
