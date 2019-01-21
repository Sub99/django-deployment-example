from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')


def users(request):

    us_list = User.objects.order_by('first_name')
    my_dict = {'user_list': us_list}
    return render(request,'AppTwo/users.html',context=my_dict)
