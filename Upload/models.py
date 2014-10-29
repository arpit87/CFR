from django.db import models

# Create your models here.
class Contacts(models.Model):
    cfrid = models.IntegerField(null=False)
    name = models.CharField(max_length=140)
    phone1 = models.IntegerField(null=True)  
    phone2 = models.IntegerField(null=True)
    phone3 = models.IntegerField(null=True)
    email1 = models.CharField(max_length=255,null=True)
    email2 = models.CharField(max_length=255,null=True)
    email3 = models.CharField(max_length=255,null=True)

    def __unicode__(self):
        return str(self.name)


class SMS(models.Model):
    cfrid = models.IntegerField(null=False)
    number = models.IntegerField(null=False)    
    date_time = models.DateTimeField(null=False)
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.number)
		
class CallLog(models.Model):
    cfrid = models.IntegerField(null=False)
    name = models.CharField(max_length=255)
    number = models.IntegerField(null=False)    
    date_time = models.DateTimeField(null=False)  
    duration = models.IntegerField(null=False) 
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.name)		
