from apitest.models import User
from rest_framework import viewsets,status
from rest_framework.request import Request
from django.http import QueryDict
from apitest.serizalizers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apitest import base

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def addUser(request):
    dict = get_parameter_dic(request)
    name = dict.get('name', '')
    phone = dict.get('phone', '')
    try:
        user = User.objects.get(phone=phone)
        return base.baseResponse(status.HTTP_400_BAD_REQUEST, '', '用户已存在.')
    except User.DoesNotExist:
        user = User(name=name, phone=phone)
        serizer = UserSerializer(user)
        user.save()
        return base.baseResponse(status.HTTP_200_OK, serizer.data, '添加用户成功.')
    user = User.objects.create()
    user.save()
    return base.baseResponse(status.HTTP_200_OK, user, '增加数据成功')

@api_view(['POST'])
def deleteUser(request):
    id = get_parameter_dic(request).get('id', '')
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response('删除成功.')
    except User.DoesNotExist:
        return Response('对象不存在.')

@api_view(['POST'])
def updateUser(request):
    reqDic = get_parameter_dic(request)
    id = reqDic.get('id')
    print('the id is ', id)
    name = reqDic.get('name')
    phone = reqDic.get('phone')
    age = reqDic.get('age')
    sex = reqDic.get('sex')
    try:
        user = User.objects.get(id=id)
        if name:
            user.name = name
        if phone:
            user.phone = phone
        if age:
            user.age = age
        if sex:
            user.sex = sex
        user.save()
        return base.baseResponse(status.HTTP_200_OK, UserSerializer(user).data, '更新成功.')
    except:
        return base.baseResponse(status.HTTP_400_BAD_REQUEST, '', '用户不存在.')

@api_view(['GET','POST'])
def getUserById(request):
    dict = get_parameter_dic(request)
    id = dict.get('id')
    try:
        user = User.objects.get(id=id)
        return base.baseResponse(status.HTTP_200_OK, UserSerializer(user).data, '获取成功')
    except User.DoesNotExist:
        return base.baseResponse(status.HTTP_400_BAD_REQUEST, '', '用不存在')

@api_view(['POST'])
def uploadFile(request):
    file = request.data.get('file')
    if file.is_valid:
        return base.baseResponse(status.HTTP_200_OK, '', '文件上传成功')
    else:
        return base.baseResponse(status.HTTP_400_BAD_REQUEST, '', '文件上传失败')

#获取参数
def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}
    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = request.data.dict()
    if query_params != {}:
        return query_params
    else:
        return result_data