from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
import random,json, redis
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
ipmaster="127.0.0.1"
def device(request,id):

    inform=redis.Redis("11.0.0.2")
    a=inform.get(id)

    b=eval(a)

    #data1=json.loads(b)
    #print data1,type(data1)

    ################  Este if es para el caso de que se necesite reiniciar un video###########################################
    #if(a[1]=="restart"):
    #    inform.set(id,+b[0]+",play")
    #print data1
    dataj=json.dumps(b)
    #d=json.loads(dataj)
    #print type(d)

    return HttpResponse(dataj)

def index(request,id):
    return render_to_response("index.html",{'id':id})
def indexlocal(request,id):
    return render_to_response("index.html",{'id':id})