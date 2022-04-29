from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from bookstore.models import Users
from bookstore.serializers import UsersSerializer


# Create your views here.
@csrf_exempt
def user_api(request, user_id=None):
    if request.method == 'GET':
        if user_id is None:
            users = Users.objects.all()
            users_serializer = UsersSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            user = Users.objects.get(id=user_id)
            users_serializer = UsersSerializer(user)
            return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("User has been added", safe=False)
        return JsonResponse("Failed!!", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(id=user_data['id'])
        departments_serializer = UsersSerializer(user, data=user_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        user = Users.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)
