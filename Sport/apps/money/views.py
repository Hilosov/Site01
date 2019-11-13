from django.shortcuts import render
from .models import Infomation
import requests

# Create your views here.

def index2(request):
    money = Infomation.objects.all()

    context = {
        'money': money
    }

    return render(request, 'money/money.html', context)