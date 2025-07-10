from django.shortcuts import render
from roll.models import Student

# Create your views here.
def home(request):
    stu=Student.objects.all()
    return render(request,'home.html',{'st':stu})