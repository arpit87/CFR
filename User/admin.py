# Register your models here.
from django.contrib import admin
from User.models import UserDetails

class UserDetailsModelAdmin(admin.ModelAdmin):
    list_display = ('cfrid','name','date_joined')


admin.site.register(UserDetails,UserDetailsModelAdmin)

