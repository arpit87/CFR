# Create your views here.
from django.http import HttpResponse

from Upload import Constants
from Upload.models import Contacts,SMS,CallLog
from Platform import utils
from Platform.views import authenticateURL
import Platform.Constants
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


#getbeep api
@csrf_exempt
def saveContacts(request):
    if authenticateURL(request)==False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    usercfrid= data[Platform.Constants.CFR_ID]
    contactArray = data[Constants.UploadConstants.CONTACTS]
    for contact in contactArray:
        contactname = contact[Constants.UploadConstants.NAME]
        allphones = contact[Constants.UploadConstants.ALLPHONES]
        allemail = contact[Constants.UploadConstants.ALLEMAILS]
        count = 0
        contactphone = ["","",""]
        contactemail = ["","",""]
        for phone in allphones:
            if count < 3:
                contactphone[count] = phone.get(Constants.UploadConstants.PHONE)
            count=count+1

        count = 0
        for email in allemail:
            if count < 3:
                contactemail[count] = email.get(Constants.UploadConstants.EMAIL)
            count = count+1

        thisContact = Contacts(cfrid=usercfrid, name=contactname,phone1=contactphone[0],phone2=contactphone[1],phone3=contactphone[2],
                               email1=contactemail[0],email2=contactemail[1],email3=contactemail[2])
        thisContact.save()

    output = dict({"ContactsSaved":len(contactArray)})
    httpresonse = utils.successJson(output)
    return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)
	
@csrf_exempt
def saveSMS(request):
    if authenticateURL(request)==False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    usercfrid= data[Platform.Constants.CFR_ID]
    smsArray = data[Constants.UploadConstants.SMS]
    for sms in smsArray:
		smsnumber = sms[Constants.UploadConstants.NUMBER]
		smstext = sms[Constants.UploadConstants.TEXT]
		smsdatetimestamp = sms[Constants.UploadConstants.DATE]
		smstype = sms[Constants.UploadConstants.TYPE]
		smsdate = datetime.fromtimestamp(float(smsdatetimestamp))
		thisSMS = SMS(cfrid=usercfrid,number=smsnumber,text=smstext,date_time=smsdate,type=smstype)
		thisSMS.save()					   						   
	    
    output = dict({"SMSSaved":len(smsArray)})
    httpresonse = utils.successJson(output)
    return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)	
	
@csrf_exempt
def saveCallLog(request):
    if authenticateURL(request)==False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    usercfrid= data[Platform.Constants.CFR_ID]
    callLogArray = data[Constants.UploadConstants.CALL_LOG]
    for call in callLogArray:
        callname = call[Constants.UploadConstants.NAME]
        callnumber = call[Constants.UploadConstants.NUMBER]
        callduration = call[Constants.UploadConstants.DURATION]
        calldaterimestamp = call[Constants.UploadConstants.DATE]
        calltype = call[Constants.UploadConstants.TYPE]
        calldate = datetime.fromtimestamp(float(calldaterimestamp))
        thisCall = CallLog(cfrid=usercfrid,name=callname, number=callnumber,duration=callduration,date_time=calldate,type=calltype)
        thisCall.save()

    output = dict({"CallLogsSaved":len(callLogArray)})
    httpresonse = utils.successJson(output)
    return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

