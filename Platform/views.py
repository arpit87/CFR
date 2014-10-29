from Platform.models import APPDATA
import Platform.Constants
import json

def authenticateURL(request):
    if(Platform.Constants.ISTESTMODE):
        return True

    data = json.loads(request.read())
    if request.method == 'POST':
        appuuid_req = data[Platform.Constants.APPUUID]
        cfrid_req = data[Platform.Constants.CFR_ID]
        appdetails = APPDATA.objects.get(cfrid = cfrid_req)
        if appdetails.appuuid == appuuid_req:
            return True


    if request.method == 'GET':
        appuuid_req = data[Platform.Constants.APPUUID]
        cfrid_req = data[Platform.Constants.CFR_ID]
        appdetails = APPDATA.objects.get(cfrid = cfrid_req)
        if appdetails.appuuid == appuuid_req:
            return True


    return False

