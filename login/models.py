from django.db import models
# Create your models here.
from leavemessage.models import leavemessage
from tiezi.models import tiezi


class people(models.Model):
    name = models.TextField(max_length=20)
    grade = models.IntegerField()
    faculty = models.IntegerField()
    numberofcollect = models.IntegerField()
    numberoflike = models.IntegerField()
    numberofpost = models.IntegerField()
    openid = models.TextField(max_length=100)
    photopaths = models.ImageField(upload_to="headpic",null=True)
    content=models.TextField(max_length=500,null=True)
    selftext=models.TextField(max_length=100)
    sex=models.TextField(max_length=5)
    liketiezi = models.ManyToManyField(tiezi,related_name="likepeople")
    collecttiezi=models.ManyToManyField(tiezi,related_name="collectpeople")
    likeleavemessage = models.ManyToManyField(leavemessage)
    text=models.TextField(max_length=120,null=True)




