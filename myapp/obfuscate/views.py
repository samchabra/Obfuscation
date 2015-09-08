from django.shortcuts import render, render_to_response, get_object_or_404
import random, string, json

import uuid
from obfuscate.models import link
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf

# Create your views here.

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('obfuscate/index.html', c)
   # return render(request,'obfuscate/index.html')
    

    
def redirectOriginal(request, obf_id):
    print("checking")
    url = get_object_or_404(link, pk = obf_id)
    url.clicks += 1
    url.save()
    print("trying to redirect")
    return HttpResponseRedirect(url.target)




def obfURLR(request):
    url = request.POST.get('url','')
    
    if not (url == ''):
        print("please?")
        obf_id = uuid.uuid4()
        print("and thanks")
        b = link(target = url, obf_id = obf_id)
        b.save()
        print("yes?")
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + obf_id
        print("final")
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}),
             content_type="application/json")

def obfUrl(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        obf_id = getShortCode()
        b = link(target=url, obf_id=obf_id)
        b.save()
        
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + obf_id
        print("working")
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}),
             content_type="application/json")


def getShortCode():
    length = 36
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        obf_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = link.objects.get(pk=obf_id)
        except:
            return obf_id

