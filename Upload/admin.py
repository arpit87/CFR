# Register your models here.
from django.contrib import admin
from Upload.models import Contacts,SMS,CallLog

class ContactsModelAdmin(admin.ModelAdmin):
    list_display = ('cfrid','name','phone1','email1','phone2','email2','phone3','email3')

class SMSModelAdmin(admin.ModelAdmin):
    list_display = ('cfrid', 'number', 'date_time', 'text','type')
	
class CallLogModelAdmin(admin.ModelAdmin):
    list_display = ('cfrid', 'name', 'number', 'date_time','duration','type')


admin.site.register(Contacts,ContactsModelAdmin)
admin.site.register(SMS,SMSModelAdmin)
admin.site.register(CallLog,CallLogModelAdmin)
