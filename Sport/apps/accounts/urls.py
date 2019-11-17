from django.urls import path
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]