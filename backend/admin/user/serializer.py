from rest_framework import serializers
from .models import userVo as user

class userSerializer(serializers.serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    birth = serializers.CharField()
    address = serializers.CharField()
    class Meta :
        model : user
        fileds = '__all__'

        def create(self, validated_date):
            return user.objects.create(**validated_date)

        def update(self, instance, validated_date):
            user.objects.filter(pk=instance.username).update(**validated_date)