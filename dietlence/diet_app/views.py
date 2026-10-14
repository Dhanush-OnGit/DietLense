from django.shortcuts import render
from diet_app.serializer import *
from diet_app.models import *
from diet_app.utility_func import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,ListAPIView,DestroyAPIView
from diet_app.permission import IsOwner,IsDeleteOwner
# Create your views here.

class SignupView(CreateAPIView):
    serializer_class = UserSerializer

class ProfileView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerilaizer

    def perform_create(self, serializer):
        user = self.request.user
        # data = serializer.validated_data
        # print(data)
        # bmr =  calculate_bmr(
        #     age=data.get('age'),
        #     heigth=data.get('heigth'),
        #     weigth=data.get('weigth'),
        #     gender=data.get('gender'),
        #     activity_level=data.get('activity_level')
        # )
        return serializer.save(owner =user)

class ProfileRetriveView(RetrieveAPIView,UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    serializer_class = ProfileSerilaizer
    queryset = UserProfile.objects.all()

# class ProfileUpdateView(UpdateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsOwner]
#     serializer_class = ProfileSerilaizer
#     queryset = UserProfile.objects,all()

class UserRetriveView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class FoodLogCreateView(CreateAPIView,ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class FoodLogRetriveView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class FoodLogUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()

class FoodLogDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsDeleteOwner]
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()

class DietSummaryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    def get(self,request,*args,**kwargs):
        cur_date = timezone.now()
        quuryset = FoodLog.objects.filter(created_at__date = cur_date,owner=request.user)
        calories = quuryset.values('calories').aggregate(Sum('calories'))
        print(calories)
        print(request.user.profile.bmr)
        context ={
            "total_calarie_consumed":calories.get('calories__sum'),
            "daily_target":request.user.profile.bmr,
            "balance":request.user.profile.bmr-calories.get('calories__sum')
        }
        return Response(context)

    



