from django.contrib import admin

# Register your models here.
from .models import Module, Rating, Users

admin.site.register(Module)
admin.site.register(Rating)
admin.site.register(Users)
