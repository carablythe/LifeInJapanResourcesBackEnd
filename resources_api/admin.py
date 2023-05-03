from django.contrib import admin

from . models import Resource

admin.site.register(Resource)

from . models import Forum

admin.site.register(Forum)
