from django.db import models

# Create your models here.
from leavemessage.models import leavemessage


class tiezi(models.Model):
    content=models.TextField(max_length=500)
    numoflike=models.IntegerField()
    numofcollect=models.IntegerField()
    kind=models.BooleanField()
    openid=models.TextField(max_length=100)
    ownid=models.TextField(max_length=100)
    onshow=models.BooleanField(default=True)
    name=models.TextField(max_length=20,null=True)
    numofleavemessage=models.IntegerField(default=0)
    leavemessage=models.ManyToManyField(leavemessage)
    havelike=models.BooleanField(default=False)
    havecollect=models.BooleanField(default=False)
    isqa=models.BooleanField(default=False)
