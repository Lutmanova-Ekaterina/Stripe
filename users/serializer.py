from rest_framework import serializers
from django.contrib.auth.models import make_password

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'phone',
            'password',
        )

    def create(self, validated_data):
        "хешировать пароль"
        new_user = User.objects.create(phone=validated_data['phone'], password=make_password(validated_data['password'],))
        new_user.groups.add(1) #добавляем в группу новых пользователей
        return new_user

    def update(self, instance, validated_data):
        "изменим пароль"
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
