from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^login', login),
    url(r'^student', student),
    url(r'^subject', subject),
    url(r'^final', final),
    url(r'^admitcard', admit_card),
    url(r'^logout', logout),
    url(r'^', home),
]