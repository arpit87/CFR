from django.db import models

# Create your models here.
class UserDetails(models.Model):
    cfrid = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=60)
    date_joined = models.DateField('date joined')

    def __unicode__(self):
        return self.name




