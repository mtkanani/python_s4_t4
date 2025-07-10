from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages


def signup_views(request):

    if request.method=="POST":
        form = UserCreationForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request,"signup.html"),{"form":form}
    
def login_views(request):

     if request.method=="POST":
        form = UserAuthenticationForm(request,data=request.POST)

        if form.is_valid:
            user = form.get_user()
            login(request,user)
            
            return redirect("home")
        else:
            messages.error(request,"Invalid login Info ")
     else:
         


