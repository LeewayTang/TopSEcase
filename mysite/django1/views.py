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


class LoginRegister(viewsets.GenericViewSet):
    """
    login:
    账户，邮箱，密码
    """
    queryset = User.objects.all()
    # serializer_class = LoginRegisterInfoSerializer
    # test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(responses={200: ""},
                         request_body=LoginInfoSerializer)
                         #manual_parameters=[test_param])
    @action(methods=['POST'], detail=False)
    def login(self, request):
        print(request)
        data_json = json.loads(request.body)
        print(data_json)
        Uid = data_json.get('uid')
        Pwd = data_json.get('pwd')
        print(Uid, Pwd)
        queryset = User.objects.filter(uid__contains=Uid)  # .filter(uid=Uid, mail=Mail, pwd=Pwd)
        if queryset.count() == 0:
            return Response({'msg': '用户名不存在'})
        queryset = User.objects.filter(uid__contains=Uid, pwd__contains=Pwd)
        if queryset.count() == 0:
            return Response({'msg': '密码不正确'})
        # (user_list, many=True)
        ret = {'msg': 'success'}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=RegisterInfoSerializer)
    @action(methods=['POST'], detail=True)
    def register(self, request):
        Uid = request.GET.get('uid')
        Mail = request.GET.get('mail')
        Pwd = request.GET.get('pwd')

        queryset = User.objects.filter(uid=Uid, mail=Mail, pwd=Pwd)
        return

