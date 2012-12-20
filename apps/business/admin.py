from django.contrib import admin
from nnmware.apps.business.models import *
from django.utils.translation import ugettext_lazy as _
from nnmware.core.admin import TypeBaseAdmin

class TypeEmployerProfileAdmin(TypeBaseAdmin):
    list_display = ('name','employer_type','is_radio')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = ((_("Type of employer profile"), {"fields": [('name','employer_type','is_radio'),]}),)

class TypeEmployerSphereAdmin(TypeBaseAdmin):
    list_display = ('name','employer_type')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = ((_("Type of employer sphere"), {"fields": [('name','employer_type'),]}),)

class TypeEmployerAdmin(TypeBaseAdmin):
    list_display = ('name','order_in_list')
    fieldsets = (
        (_("Type of employer"), {"fields": [('name','order_in_list'),
                                            ]}),)
    ordering = ('-order_in_list','name',)


admin.site.register(TypeEmployer, TypeEmployerAdmin)
admin.site.register(TypeEmployerProfile, TypeEmployerProfileAdmin)
admin.site.register(TypeEmployerSphere, TypeEmployerSphereAdmin)
