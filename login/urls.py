from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from design import settings
from login.views import getform, test, getone, changeform, saveone

urlpatterns = [
    path('sumbit/',getform),
    path('test/',test),
    path('getone/',getone),
    path('change/',changeform),
    path('saveone/',saveone)
]
