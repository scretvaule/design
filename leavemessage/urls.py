from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from design import settings
from leavemessage.views import *
from login.views import getform, test

urlpatterns = [
path('createleavemessage/',createleavemessage),
path('deleteleavemessage/',deleteleavemessage),
path('likeleavemessage/',likeleavemessage),
path('deletelikeleavemessage/',deletelikeleavemessage),
path('getonetiezileavemessage/',getonetiezileavemessage),
path("likemyall/",likemyall),
path('getlikeleavemessage/',getlikeleavemessage),
path('getonetiezilikeleavemessage/',getonetiezilikeleavemessage),
path('getmyleavemessage/',getmyleavemessage),
]