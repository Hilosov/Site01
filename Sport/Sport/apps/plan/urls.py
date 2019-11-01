from django.urls import path
from . import views


urlpatterns = [
	path('weather',views.weather, name = 'Weather'),
	path('',views.plan, name = 'plans'),
]

	