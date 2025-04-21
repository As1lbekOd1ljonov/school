from rest_framework import serializers

from .models import User, Admin, Teacher, Student

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['role']


class AdminSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Admin
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, role='admin')
        user.set_password(password)
        user.save()

        admin = Admin.objects.create(user=user, **validated_data)
        return admin

    def update(self, instance, validated_data):
        user = instance.user
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class TeacherSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Teacher
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, role='teacher')
        user.set_password(password)
        user.save()

        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

    def update(self, instance, validated_data):
        user = instance.user
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance



class StudentSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data, role='student')
        user.set_password(password)
        user.save()

        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user = instance.user
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance