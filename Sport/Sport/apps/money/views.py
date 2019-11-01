from django.shortcuts import render
import requests

# Create your views here.

def money(request):
    return render(request, 'money/money.html')