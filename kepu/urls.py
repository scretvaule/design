from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from design import settings
from login.views import getform
from kepu.views import *

urlpatterns = [
    # path('test/',test),
    path('createone/',createone),
    # path('deleteone/',deleteone),
    # path('likeone/',likeone),
    # path('deletelikeone/',deletelikeone),
    # path('collectone/',collectone),
    # path('deletecollectone/',deletecollectone),
    # path('getall/',getall),
    # path('getmyall/',getmyall),
    # path('likemyall/',likemyall),
    # path('collectmyall/',collectmyall),
    # path('mylikeall/',mylikeall),
    # path('mycollectall/',mycollectall)
]