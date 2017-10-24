from apitest.models import User
from rest_framework import viewsets
from apitest.serizalizers import  UserSerializer
from rest_framework.response import  Response
from rest_framework.decorators import api_view

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def addUser(request, name):
    user = User.objects.create(name=name)
    user.save()
    return Response('增加数据成功')
