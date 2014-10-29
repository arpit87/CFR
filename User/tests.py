from django.test import TestCase



#Test models
from django.utils import timezone

from User.models import UserDetails

class UserDetailsTestCase(TestCase):
    def setUp(self):
        UserDetails.objects.create(cfrid= 1,name="Arpit" ,date_joined=timezone.now().date())
        UserDetails.objects.create(cfrid= 2,name="Anshul" ,date_joined=timezone.now().date())
        UserDetails.objects.create(cfrid= 3,name="Varun" ,date_joined=timezone.now().date())

    def test_userdetails(self):
        arpitdetails = UserDetails.objects.get(cfrid = 1)
        self.assertEqual(arpitdetails.name , "Arpit")




#Test URLS
from Platform.models import APPDATA
import json
import Platform.Constants

class UserAPITestCase(TestCase):
    def setUp(self):
        APPDATA.objects.create(appuuid = "123",cfrid=1)

    def test_createUser(self):
        input = json.dumps({Platform.Constants.NAME:'Arpit', Platform.Constants.APPUUID:'123'})
        response = self.client.post('/User/createUser/',input,Platform.Constants.RESPONSE_JSON_TYPE)
        self.assertEqual(response.status_code,200)
        print(response.content)