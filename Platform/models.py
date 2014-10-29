from django.db import models

# Create your models here.
class APPDATA(models.Model):
    appuuid = models.CharField(max_length=20)
    cfrid = models.IntegerField()

    def __unicode__(self):
        return self.appuuid
