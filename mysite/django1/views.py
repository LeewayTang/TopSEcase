from rest_framework import viewsets
from rest_framework import generics
from django1.models import *
from django1.serializers import *
from drf_yasg import openapi
import json
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.decorators import action


# Create your views here.
# swagger_schema = None 忽略整个class

# @method_decorator(
#     name="list",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     )
# )
class UserInfoView(viewsets.ModelViewSet):
    """
        retrieve:
            返回一组（查）

        list:
            返回所有组（查）

        create:
            创建新组（增）

        delete:
            删除现有的一组（删）

        partial_update:
            更新现有组中的一个或多个字段（改：部分更改）

        update:
            更新一组（改：全部更改）
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer

# 防止ModelViewSet的多余接口
# @method_decorator(
#     name="list",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="update",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="destroy",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="create",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="partial_update",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="retrieve",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
class Login(viewsets.GenericViewSet):
    queryset = User.objects.all#.filter(uid=Uid, mail=Mail, pwd=Pwd)
    serializer_class = LoginInfoSerializer
    @action(methods=['GET'], detail=True)
    def login(self, request):
        # """
        #     账户，邮箱，密码
        # """
        Uid = request.GET.get('uid')
        Mail = request.GET.get('mail')
        Pwd = request.GET.get('pwd')
        queryset = User.objects.filter(uid=Uid, mail=Mail, pwd=Pwd)  # .filter(uid=Uid, mail=Mail, pwd=Pwd)
        serializer_class = LoginInfoSerializer
        # (user_list, many=True)
        # return Response(serializer_class.data)



