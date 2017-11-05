from rest_framework.response import Response

def baseResponse(code,data,msg):
    return Response({'code': code, 'data': data, 'msg': msg})