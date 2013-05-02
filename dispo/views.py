# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
import random,json, redis
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

def device(request,id):

    inform=redis.Redis("localhost")
    a=inform.get(id)
    b=a.split(",")
    data=({"url":b[0],"reproduce":b[1],"tipo":b[2]})

    if(b[1]=="restart"):
        inform.set(id,+b[0]+",play")

    dataj=json.dumps(data)

    return HttpResponse(dataj,mimetype='application/json')

def index(request,id):
    return render_to_response("index.html",{'id':id})
def indexlocal(request,id):
    return render_to_response("index.html",{'id':id})