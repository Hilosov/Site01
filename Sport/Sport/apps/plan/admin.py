from django.contrib import admin
from .models import City
from .models import MainContent


admin.site.register(City)
admin.site.register(MainContent)

#class PlanAdmin(admin.ModelAdmin):
#	fields = ['article_image']
