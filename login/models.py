import datetime

from django.db import models
# Create your models here.
from django.utils import timezone

from leavemessage.models import leavemessage
from tiezi.models import tiezi


class people(models.Model):
    name = models.TextField(max_length=20)
    numberofcollect = models.IntegerField()
    numberoflike = models.IntegerField()
    numberofpost = models.IntegerField()
    weight=models.DecimalField(decimal_places=2,max_digits=8)
    height=models.DecimalField(decimal_places=2,max_digits=8)
    bir=models.DateField(default=timezone.now)
    openid = models.TextField(max_length=100)
    familyid=models.IntegerField()
    photopaths = models.ImageField(upload_to="headpic",null=True)
    content=models.TextField(max_length=500,null=True)
    sex=models.TextField(max_length=5)
    liketiezi = models.ManyToManyField(tiezi,related_name="likepeople")
    collecttiezi=models.ManyToManyField(tiezi,related_name="collectpeople")
    likeleavemessage = models.ManyToManyField(leavemessage)
    text=models.TextField(max_length=120,null=True)
    bingshi=models.TextField(max_length=120,null=True)




