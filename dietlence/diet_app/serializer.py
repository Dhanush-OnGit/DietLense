from rest_framework import serializers
from diet_app.models import *

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ["id","username","email","password","phone","profile"]
        read_only_fileds = ["id"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def get_profile(self,obj):
        profile_obj = UserProfile.objects.get(owner=obj)
        serializer_obj = ProfileSerilaizer(profile_obj)
        return serializer_obj.data

class ProfileSerilaizer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["id","owner","bmr"]

class FoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLog
        fields = "__all__"
        read_only_fields = ["id","owner","created_at"]