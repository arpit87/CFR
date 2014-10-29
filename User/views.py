# Create your views here.
import string

from django.http.response import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from Platform import utils
from Platform.models import APPDATA

from User.models import UserDetails
from Platform.views import authenticateURL
import Platform.Constants
import json




@csrf_exempt
def createUser(request):
    if authenticateURL(request) == False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse, content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    name_req = data[Platform.Constants.NAME]
    uuid_req = data[Platform.Constants.APPUUID]
    datejoined_req = timezone.now().date()
    newuser = UserDetails(name=name_req, date_joined=datejoined_req)
    newuser.save()

    #enter authentication data
    authdata = APPDATA(appuuid=uuid_req, cfrid=newuser.cfrid)
    authdata.save()   

    jsondata = dict({Platform.Constants.CFR_ID:newuser.cfrid})
    httpoutput = utils.successJson(jsondata)
    return HttpResponse(httpoutput,content_type=Platform.Constants.RESPONSE_JSON_TYPE)
