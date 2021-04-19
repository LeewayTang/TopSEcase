from rest_framework import serializers
from django1.models import *

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all_'