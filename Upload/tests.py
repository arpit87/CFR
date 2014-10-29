# Create your tests here.
#teST MODELS
from django.test import TestCase
from Upload import Constants
import json

class saveData(TestCase):
    def test_saveContacts(self):
        phones = [{Constants.UploadConstants.ALLPHONES:"976946541"},{Constants.UploadConstants.ALLPHONES:"976946541"}]
        emails = [{Constants.UploadConstants.EMAIL:"arpit87@gmail.com"},{Constants.UploadConstants.EMAIL:"arpitfarji@gmail.com"}]
        acontact = dict({Constants.UploadConstants.NAME:"Arpit",
							Constants.UploadConstants.ALLPHONES:phones,
							Constants.UploadConstants.ALLEMAILS:emails})
        contactlist = [acontact,acontact,acontact]
        contactlistobj = dict({"cfrid":21,"contacts":contactlist})
        input = json.dumps(contactlistobj)
        response = self.client.post('/Upload/saveContacts/',input, 'application/json')
        self.assertEqual(response.status_code,200)
        print response.content

    def test_saveSMS(self):
        asms = dict({Constants.UploadConstants.NUMBER:"987654231",
                     Constants.UploadConstants.DATE:"1414601769",
					 Constants.UploadConstants.TEXT:"heya wassup",
                     Constants.UploadConstants.TYPE:"inbox"})
        smslist = [asms,asms,asms]
        smslistobj = dict({"cfrid":21,"sms":smslist})
        input = json.dumps(smslistobj)
        response = self.client.post('/Upload/saveSMS/',input, 'application/json')
        self.assertEqual(response.status_code,200)
        print response.content

    def test_saveCallLog(self):
        acalllog = dict({Constants.UploadConstants.NAME:"Arpit",
                         Constants.UploadConstants.NUMBER:"987654231",
                         Constants.UploadConstants.DATE:"1414601769",
					     Constants.UploadConstants.DURATION:234,
                         Constants.UploadConstants.TYPE:"RECEIVED"})
        callloglist = [acalllog,acalllog,acalllog]
        callloglistobj = dict({"cfrid":21,"calllog":callloglist})

        input = json.dumps(callloglistobj)        
        response = self.client.post('/Upload/saveCallLog/',input, 'application/json')
        self.assertEqual(response.status_code,200)
        print response.content


