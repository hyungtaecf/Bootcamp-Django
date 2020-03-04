from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def help(request):
    help_dict = {'insert_help':"I am in help view!"}
    return render(request,'AppTwo/help.html', context = help_dict)

def users(request):
    user_list = User.objects.order_by("email")
    user_dict = {'user_list':user_list}
    return render(request,'AppTwo/users.html', context = user_dict)
