from django.db import models

# Create your models here.
class leavemessage(models.Model):
    openid=models.TextField(max_length=50,default="000000")
    text=models.TextField(max_length=120)
    ownid=models.TextField(max_length=50)
    numberoflike=models.IntegerField(default=0)
    onshow=models.BooleanField(default=True)
    name=models.TextField(max_length=20,null=True)
    content=models.TextField(max_length=150,null=True)
    havelike=models.BooleanField(default=False)

