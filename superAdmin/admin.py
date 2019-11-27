from django.contrib import admin
from .models import CompanyType,Exp,Education

# Register your models here.

@admin.register(CompanyType)
class SuperAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "公用信息"
    list_display = ['typename']

@admin.register(Exp)
class SuperAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "工作经验"

    list_display = ['con']

@admin.register(Education)
class SuperAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "教育经验"

    list_display = ['con']