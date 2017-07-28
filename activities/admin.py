from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import SportrotterUser
from .models import *

admin.site.register(Activity)
admin.site.register(Location)
admin.site.register(Feedback)
admin.site.register(ActivityRegistration)
# admin.site.register(SportrotterUser, UserAdmin)
