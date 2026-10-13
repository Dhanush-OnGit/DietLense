from django.db import models
from django.contrib.auth.models import AbstractUser
from diet_app.utility_func import calculate_bmr
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15,unique=True)

class UserProfile(models.Model):
    age = models.PositiveIntegerField()
    weigth = models.FloatField()
    heigth = models.PositiveIntegerField()

    GENDER_OPTIONS = [
        ('Male','male'),
        ('Female','female')
    ]
    gender = models.CharField(choices=GENDER_OPTIONS,max_length=20,default='male')
    ACTIVITY_OPTIONS =[
        ('1.2','sedentary (title/no excersise)'),
        ('1.375','Lightly active (excercise 1-3 days/week)'),
        ('1.55','Moderately active (excercise 3-5 days/week)'),
        ('1.725','very active (excesice 6-7 days/week)'),
        ('1.9','Extra active (very intence activity)')
    ]
    activity_level = models.CharField(max_length=200,choices=ACTIVITY_OPTIONS,default='1.2')
    bmr = models.FloatField(null=True)
    owner = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")

    def save(self,*args,**kwargs):
        self.bmr = calculate_bmr(self.age,self.weigth,self.heigth,self.gender,float(self.activity_level))
        return super().save(*args,**kwargs)


class FoodLog(models.Model):
    name = models.CharField(max_length=200,null=True)
    MEAL_TYPE=[
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('snack','Snack')
    ]
    meal_type = models.CharField(max_length=50,choices=MEAL_TYPE,null=True)
    calories = models.PositiveIntegerField()
    serving_size = models.CharField(max_length=100,null=True)
    notes = models.TextField(null=True)
    picture = models.ImageField(upload_to='foodlog',null=True)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="foodLog")
    created_at = models.DateTimeField(auto_now_add=True)
