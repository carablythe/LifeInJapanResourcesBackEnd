from django.contrib import admin

# Register your models here.
from .models import Resource
admin.site.register(Resource)

from .models import Forum
admin.site.register(Forum)
