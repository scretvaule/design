import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from login.models import people


def getform(request):
    if request.method=='POST':
        name=request.POST['name']
        sex=request.POST['sex']
        photopaths=request.FILES.get('photopaths')
        numberoflike=request.POST['numberoflike']
        numberofpost=request.POST['numberofpost']
        openid=request.POST['openid']
        numberofcollect=request.POST['numberofcollect']
        weight=request.POST['weight']
        height = request.POST['height']
        binshi=request.POST["binshi"]
        bir=request.POST['bir']
        familyid=request.POST['familyid']
        people.objects.create(name=name,familyid=familyid,sex=sex,weight=weight,bingshi=binshi,bir=bir,height=height,photopaths=photopaths,numberoflike=numberoflike,numberofpost=numberofpost,openid=openid,numberofcollect=numberofcollect)
        return HttpResponse("success")
    else:
        return HttpResponse("fail")

def changeform(request):
    if request.method=='POST':
        name=request.POST['name']
        sex=request.POST['sex']
        faculty=request.POST['faculty']
        grade=request.POST['grade']
        photopaths=request.FILES.get('photopaths')
        selftext=request.POST['selftext']
        numberoflike=request.POST['numberoflike']
        numberofpost=request.POST['numberofpost']
        openid=request.POST['openid']
        numberofcollect=request.POST['numberofcollect']
        person=people.objects.filter(openid=openid)[0]
        person.name=name
        person.sex=sex
        person.faculty=faculty
        person.grade=grade
        person.photopaths=photopaths
        person.selftext=selftext
        person.numberoflike=numberoflike
        person.numberofpost=numberofpost
        person.numberofcollect=numberofcollect
        person.save()
        return HttpResponse("success")
    else:
        return HttpResponse("fail")

def getone(request):
    if request.method=="POST":
        openid=request.POST['openid']
        peopleinfo=people.objects.filter(openid=openid)
        if(len(peopleinfo)!=0):
            return HttpResponse(serializers.serialize("json", peopleinfo))
        else:
            return HttpResponse("fail")

def saveone(request):
    if request.method=="POST":
        name = request.POST['name']
        sex = request.POST['sex']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        photopaths = request.FILES.get('photopaths')
        selftext = request.POST['selftext']
        openid = request.POST['openid']
        peopleinfo=people.objects.filter(openid=openid)[0]
        peopleinfo.name=name
        peopleinfo.sex=sex
        peopleinfo.faculty=faculty
        peopleinfo.grade=grade
        peopleinfo.photopaths=photopaths
        peopleinfo.selftext=selftext
        peopleinfo.save()
        return HttpResponse("success")

def test(request):
    data = serializers.serialize("json", people.objects.all())#fields表示要啥数据
    return HttpResponse(data)