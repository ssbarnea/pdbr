from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = [
    url("", lambda request: HttpResponse()),
]
