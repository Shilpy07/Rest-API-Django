from django.contrib import admin
from ajax.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'age')
    search_fields = ('name', 'email', 'gender', 'age')

admin.site.register(Profile, ProfileAdmin)