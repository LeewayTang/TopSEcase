from rest_framework import viewsets
from rest_framework import generics
from django1.models import *
from django1.serializers import *


# Create your views here.

class UserInfoView(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializers_cla = UserInfoSerializer
    pass



