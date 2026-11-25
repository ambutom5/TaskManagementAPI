from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from TaskRepo.models import TaskDb
from TaskRepo.serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SignUpView(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"User Registration Successfull!","Details":serializer_instance.data})
        else:
            return Response(serializer_instance.errors)

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        qs = User.objects.all()
        serializer_instance = UserSerializer(qs,many=True)
        return Response(serializer_instance.data)


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        qs = TaskDb.objects.filter(user=request.user)
        serializer_instance = TaskSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance = TaskSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class TaskretrieveUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        qs = get_object_or_404(TaskDb,id=pk,user=request.user)
        serializer_instance = TaskSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk):
        qs = get_object_or_404(TaskDb,id=pk,user=request.user)
        serializer_instance = TaskSerializer(qs,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk):
        qs = get_object_or_404(TaskDb,id=pk,user=request.user)
        qs.delete()
        return Response({"Message":"Task Deleted!"})


    

