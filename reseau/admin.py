from django.contrib import admin
from authentication.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'groupe')

admin.site.register(User)