from django.contrib import admin
from .models import CompanyUser,Job

# Register your models here.

@admin.register(CompanyUser)
class CompanyAdmin(admin.ModelAdmin):
    fields = ('name','type','info','tel')
    list_display = ('name','type','info','user','tel')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)





@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    exclude = ('cid',)
    list_display = ('cid','name','info','eid','edu_id')
    fieldsets = (
        ("职位信息",{
            'fields':('name','info')
        }),
        ('职位要求',{
            'fields':('eid','edu_id')
        }),
        ('职位待遇',{
            'fields':('low_pay','hig_pay')
        }),
        ('工作地址',{
            'fields':('Provincial','city','area','address')
        })
    )
    pass
    def save_model(self, request, obj, form, change):

        obj.cid = request.user.companyuser
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(cid=request.user.companyuser.id)