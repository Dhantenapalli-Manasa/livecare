from django.contrib import admin
from .models import user, AdminUser

admin.site.register(user)
admin.site.register(AdminUser)
# Register your models here.
