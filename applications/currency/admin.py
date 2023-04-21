from django.contrib import admin

from applications.currency.models import *

# Register your models here.
admin.site.register(Organisations)
admin.site.register(Currency)
admin.site.register(Comment)
admin.site.register(Rating)