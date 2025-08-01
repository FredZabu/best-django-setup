from django.contrib import admin
from .forms import customUserCreationForm, CustomUserChangeForm
from .models import customUser


class CustomUserAdmin(admin.ModelAdmin):
    add_form = customUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']
    
admin.site.register(customUser, CustomUserAdmin)
