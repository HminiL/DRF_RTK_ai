from django.http import JsonResponse
from django.shortcuts import render
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.user.models import User
from admin.user.serializer import UserSerializer


@api_view(['GET','POST','PUT'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data = serializer, safe = False)
    elif request.method == 'POST':
        # ic('========== 회원가입 진입 ===============')
        new_user = request.data #['body']
        ic(new_user)
        serializer = UserSerializer(data = new_user) #['user']
        if serializer.is_valid():
            # serializer.save()
            return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':

        return None

@api_view(['GET','POST'])
def remove(request, id):
    pass

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try :
        loginUser = request.data
        # ic(type(loginUser)) :  <class 'dict'>
        ic(loginUser['password'])
        dbUser = User.objects.get(pk=loginUser['username'])
        # ic(type(dbUser)) : <class 'admin.user.models.User'>
        # ic(dbUser)
        # ic(dbUser.password)
        if loginUser['password'] == dbUser.password:
            print('**************** 로그인 성공')
            userSerializer = UserSerializer(dbUser, many=False) # 리턴하는 유저가 한명 따라서 False, 리스트를 리턴하면 True
            ic(UserSerializer)
            return JsonResponse(data=userSerializer.data, safe=False)
            # return serializer = UserSerializer(loginUser, many=True)
        else:
            print('**************** 비밀번호 오류')
            return JsonResponse(data ={'result':'PASSWORD-FAIL'}, status=201)
    except User.DoesNotExist :
        print('*'*100)
        print('**************** Username 오류')
        return JsonResponse(data ={'result':'USERNAME-FAIL'}, safe = False)



    # serializer = UserSerializer(data = request.data)
    # serializer.is_valid(raise_exception=True)
    #
    # user = serializer.validated_data
    # ic(user)
    # return JsonResponse({
    #     "user":serializer
    # })
