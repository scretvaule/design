import json
from itertools import chain

from django.db import connection
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from tiezi.models import tiezi
from login.models import people

def createone(request):
    if request.method=='POST':
        content=request.POST['content']
        numoflike=request.POST['numoflike']
        numofcollect=request.POST['numofcollect']
        kind=request.POST['kind']
        openid=request.POST['openid']
        ownid=request.POST['ownid']
        isqa=request.POST['isqa']
        name=people.objects.filter(openid=openid)[0].name
        tiezi.objects.create(content=content,numoflike=numoflike,numofcollect=numofcollect,kind=kind,openid=openid,ownid=ownid,name=name,isqa=isqa)
        return HttpResponse("success")

def deleteone(request):
    ownid=request.GET.get("ownid")
    tie=tiezi.objects.filter(ownid=ownid)[0]
    tie.onshow=False
    tie.save()
    return HttpResponse("success")


def likeone(request):
    ownid=request.GET.get("ownid")
    openid=request.GET.get("openid")
    onetie=tiezi.objects.filter(ownid=ownid)[0]
    onetie.numoflike=onetie.numoflike+1
    onetie.save()
    person=people.objects.filter(openid=onetie.openid)[0]
    person.numberoflike=person.numberoflike+1
    person.save()
    person = people.objects.filter(openid=openid)[0]
    onetie.likepeople.add(person)
    return HttpResponse(onetie.numoflike)

def deletelikeone(request):
    ownid=request.GET.get("ownid")
    openid=request.GET.get("openid")
    onetie=tiezi.objects.filter(ownid=ownid)[0]
    onetie.numoflike=onetie.numoflike-1
    onetie.save()
    person=people.objects.filter(openid=onetie.openid)[0]
    person.numberoflike=person.numberoflike-1
    person.save()
    person = people.objects.filter(openid=openid)[0]
    onetie.likepeople.remove(person)
    return HttpResponse("success")

def collectone(request):
    ownid = request.GET.get("ownid")
    openid = request.GET.get("openid")
    onetie = tiezi.objects.filter(ownid=ownid)[0]
    onetie.numofcollect = onetie.numofcollect + 1
    onetie.save()
    person = people.objects.filter(openid=onetie.openid)[0]
    person.numberofcollect = person.numberofcollect + 1
    person.save()
    person = people.objects.filter(openid=openid)[0]
    onetie.collectpeople.add(person)
    return HttpResponse("success")

def deletecollectone(request):
    ownid=request.GET.get("ownid")
    openid=request.GET.get("openid")
    onetie=tiezi.objects.filter(ownid=ownid)[0]
    onetie.numofcollect=onetie.numofcollect-1
    onetie.save()
    person=people.objects.filter(openid=onetie.openid)[0]
    person.numberofcollect=person.numberofcollect-1
    person.save()
    person = people.objects.filter(openid=openid)[0]
    onetie.collectpeople.remove(person)
    return HttpResponse("success")

def getall(request):
    openid=request.GET.get('openid')
    sss = request.GET.get('sss')
    person=people.objects.filter(openid=openid)[0]
    liketiezi=person.liketiezi.filter(onshow=True)
    collecttiezi=person.collecttiezi.filter(onshow=True)
    if sss==None:
        all = tiezi.objects.filter(onshow=True)
    else:
        all=tiezi.objects.filter(onshow=True).filter(name__contains=sss)
    for i in all:
        if i in liketiezi:
            i.havelike=True
        if i in collecttiezi:
            i.havecollect=True
    return HttpResponse(serializers.serialize("json",all ))


def getmyall(request):
    openid=request.GET.get("openid")
    return HttpResponse(serializers.serialize("json", tiezi.objects.filter(Q(openid=openid)|Q(onshow=True))))

def likemyall(request):
    openid = request.GET.get("openid")
    tiezis=tiezi.objects.filter(Q(openid=openid)|Q(onshow=True))
    myall=tiezis[0].likepeople.all()
    for i in myall:
        i.content=tiezis[0].content
    newall=None
    for i in range(1,tiezis.count()):
        newall=tiezis[i].likepeople.all()
        for k in newall:
            k.content=tiezis[i].content
        myall=chain(myall,newall)
    return HttpResponse(serializers.serialize("json", myall))

def collectmyall(request):
    openid = request.GET.get("openid")
    tiezis=tiezi.objects.filter(Q(openid=openid)|Q(onshow=True))
    myall=tiezis[0].collectpeople.all()
    for i in myall:
        i.content = tiezis[0].content
    newall = None
    for i in range(1, tiezis.count()):
        newall = tiezis[i].collectpeople.all()
        for k in newall:
            k.content = tiezis[i].content
        myall = chain(myall, newall)
    return HttpResponse(serializers.serialize("json", myall))

def mylikeall(request):
    openid = request.GET.get("openid")
    person=people.objects.filter(openid=openid)[0]
    return HttpResponse(serializers.serialize("json", person.liketiezi.filter(onshow=True)))

def mycollectall(request):
    openid = request.GET.get("openid")
    person=people.objects.filter(openid=openid)[0]
    return HttpResponse(serializers.serialize("json", person.collecttiezi.filter(onshow=True)))

def test(request):
    he=serializers.serialize("json", people.objects.all())
    a=serializers.serialize("json", people.objects.all()[0:1])
    return HttpResponse(a)