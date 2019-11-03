from django.shortcuts import render

def index(request):

	return render(request, 'articles/index1.html')
