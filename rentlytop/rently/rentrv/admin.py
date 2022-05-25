from django.contrib import admin
from . import models

admin.site.register(models.Rv)
admin.site.register(models.Renter)
admin.site.register(models.Rent)
