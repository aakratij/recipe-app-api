from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['name','email']
    fieldsets = (
        ('None',{'fields' : ('email' , 'password' )}),
        ( _('Personal_Info'),{'fields' : ('name',)}),
        ( _('Permissions'),{'fields' : ('is_superuser','is_staff','is_active')}),
        ( _('Important dates'),{'fields' : ('last_login',)})
    )
    add_fieldsets = (
        (None , {
            'classes' : ('wide',),
            'fields' :  ('email','password1','password2')
        }),
    )

admin.site.register(models.User,UserAdmin)