"""Sport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.defaults import page_not_found
import django


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

urlpatterns = [
    path('plan/', include('plan.urls')),
    path('', include('homepage.urls')),
	path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('money/', include('money.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),

    #http
    path('404/', custom_page_not_found)
]

if settings.DEBUG:
    urlpatterns+= staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )