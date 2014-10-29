from django.conf.urls import patterns,url
from Upload import views

urlpatterns = patterns('',
                       url(r'^saveContacts/',views.saveContacts,name='savecontact'),
                       url(r'^saveSMS/',views.saveSMS,name='savesms'),
                       url(r'^saveCallLog/',views.saveCallLog,name='savecalllog'),                       
                        )