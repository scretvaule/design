from itertools import chain

from django.db.models import Q
from django.shortcuts import render
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from leavemessage.models import leavemessage
from login.models import people

# Create your views here.
from tiezi.models import tiezi


def createleavemessage(request):
    tieziownid=request.POST['tieziownid']
    onetiezi=tiezi.objects.filter(ownid=tieziownid)[0]
    openid=request.POST['openid']
    text=request.POST['text']
    ownid=request.POST['ownid']
    numberoflike=request.POST['numberoflike']
    person=people.objects.filter(openid=openid)[0]
    name=person.name
    oneleavemssage=leavemessage.objects.create(openid=openid,text=text,ownid=ownid,numberoflike=numberoflike,name=name)
    onetiezi.leavemessage.add(oneleavemssage)
    return HttpResponse("success")

def deleteleavemessage(request):
    ownid = request.GET.get('ownid')
    oneleavemeaage=leavemessage.objects.filter(ownid=ownid)[0]
    oneleavemeaage.onshow=False
    oneleavemeaage.save()
    return HttpResponse("success")

def likeleavemessage(request):
    ownid = request.GET.get('ownid')
    oneleavemessage=leavemessage.objects.filter(ownid=ownid)[0]
    oneleavemessage.numberoflike=oneleavemessage.numberoflike+1
    oneleavemessage.save()
    person=people.objects.filter(openid=oneleavemessage.openid)[0]
    person.numberoflike=person.numberoflike+1
    person.save()
    oneleavemessage.people_set.add(person)
    return HttpResponse("success")

def deletelikeleavemessage(request):
    ownid = request.GET.get('ownid')
    oneleavemessage=leavemessage.objects.filter(ownid=ownid)[0]
    oneleavemessage.numberoflike=oneleavemessage.numberoflike-1
    oneleavemessage.save()
    person=people.objects.filter(openid=oneleavemessage.openid)[0]
    person.numberoflike=person.numberoflike-1
    person.save()
    oneleavemessage.people_set.remove(person)
    return HttpResponse("success")

def likemyall(request):
    openid = request.GET.get("openid")
    leavemessages=leavemessage.objects.filter(Q(openid=openid)|Q(onshow=True))
    myall=leavemessages[0].people_set.all()
    for i in myall:
        i.content=leavemessages[0].tiezi_set.all()[0].content
        i.text=leavemessages[0].text
    newall=None
    for i in range(1,leavemessages.count()):
        newall=leavemessages[i].people_set.all()
        for k in newall:
            k.content = leavemessages[i].tiezi_set.all()[0].content
            k.text=leavemessages[i].text
        myall=chain(myall,newall)
    return HttpResponse(serializers.serialize("json", myall))

def getonetiezileavemessage(request):
    tieziownid = request.POST['tieziownid']
    openid=request.POST["openid"]
    peoples=people.objects.filter(openid=openid)[0]
    likeleavemessages=peoples.likeleavemessage.all()
    onetiezi = tiezi.objects.filter(ownid=tieziownid)[0]
    allleavemessage=onetiezi.leavemessage.filter(onshow=True)
    for i in allleavemessage:
        if i in likeleavemessages:
            i.havelike=True
    return HttpResponse(serializers.serialize('json',allleavemessage))

def getlikeleavemessage(request):
    openid = request.GET.get("openid")
    person=people.objects.filter(openid=openid)[0]
    return HttpResponse(serializers.serialize('json',person.likeleavemessage.filter(onshow=True)))

def getonetiezilikeleavemessage(request):
    openid = request.POST['openid']
    person=people.objects.filter(openid=openid)[0]
    tieziownid = request.POST['tieziownid']
    onetiezi = tiezi.objects.filter(ownid=tieziownid)[0]
    info=onetiezi.leavemessage.all()&person.likeleavemessage.all()
    return HttpResponse(serializers.serialize('json', info))

def getmyleavemessage(request):
    openid = request.GET.get('openid')
    tiezis=tiezi.objects.filter(Q(openid=openid)|Q(onshow=True))
    myall = tiezis[0].leavemessage.all()
    for i in myall:
        i.content=tiezis[0].content
    newall = None
    print(myall.count())
    for i in range(1, tiezis.count()):
        newall = tiezis[i].leavemessage.all()
        for k in newall:
            k.content = tiezis[i].content
        myall = chain(myall, newall)
    return HttpResponse(serializers.serialize("json", myall))
