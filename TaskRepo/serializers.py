from rest_framework import serializers
from django.contrib.auth.models import User
from TaskRepo.models import TaskDb

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","username","password","email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDb
        fields = "__all__"
        read_only_fields = ["user"]
