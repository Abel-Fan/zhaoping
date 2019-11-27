from django.db import models

# Create your models here.

class CompanyType(models.Model):
    class Meta:
        verbose_name = "公司类型"
        verbose_name_plural = "公司类型"
    typename = models.CharField(max_length=20,verbose_name="公司类型")
    def __str__(self):
        return self.typename

class Exp(models.Model):
    class Meta:
        verbose_name = "工作年限"
        verbose_name_plural = "工作年限"
    con = models.CharField(max_length=10,verbose_name="工作年限")
    def __str__(self):
        return self.con

class Education(models.Model):
    class Meta:
        verbose_name = "教育背景"
        verbose_name_plural = "教育背景"
    con = models.CharField(max_length=10, verbose_name="学历")
    def __str__(self):
        return self.con
class Provincial(models.Model):
    class Meta:
        db_table = "provinces"
    provinceid = models.IntegerField(verbose_name="省编码",unique=True)
    province = models.CharField(max_length=100, verbose_name="省")
    def __str__(self):
        return self.province

class City(models.Model):
    class Meta:
        db_table ="cities"
    cityid = models.CharField(max_length=6, verbose_name="城市编码",unique=True)
    city = models.CharField(max_length=40, verbose_name="城市名称")
    provinceid = models.ForeignKey(Provincial,to_field="provinceid",on_delete=models.CASCADE)
    def __str__(self):
        return self.city

class Area(models.Model):
    class Meta:
        db_table = "areas"
    areaid = models.CharField(max_length=6,verbose_name="区县编码")
    area = models.CharField(max_length=40,verbose_name="区县名称")
    cityid = models.ForeignKey(City,to_field="cityid",on_delete=models.CASCADE)
    def __str__(self):
        return self.area


