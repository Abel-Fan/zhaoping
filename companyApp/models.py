from django.db import models
from django.core.exceptions import ValidationError
from superAdmin.models import CompanyType,Exp,Education,Provincial,City,Area

# Create your models here.

from django.contrib.auth.models import User

def tel_validators(value):
    if len(value)!=11:
        raise ValidationError("联系方式必须是11位")


# 公司职员
class CompanyUser(models.Model):
    class Meta:
        verbose_name = "公司信息"
        verbose_name_plural = "公司信息"
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="联系人")
    name = models.CharField(max_length=50,verbose_name="公司名称")
    tel = models.CharField(max_length=11,validators=[tel_validators],verbose_name="公司电话")
    info = models.CharField(max_length=200,verbose_name="公司简介")
    type = models.ForeignKey(CompanyType,on_delete=models.CASCADE,verbose_name="公司类型")
    def __str__(self):
        return self.name

# 公司岗位
class Job(models.Model):
    class Meta:
        verbose_name = "岗位"
        verbose_name_plural = "岗位"
    cid = models.ForeignKey(CompanyUser,on_delete=models.CASCADE,verbose_name="公司名称")
    name = models.CharField(max_length=20,verbose_name="职位")
    eid = models.ForeignKey(Exp,on_delete=models.CASCADE,verbose_name="经验要求")
    edu_id = models.ForeignKey(Education,on_delete=models.CASCADE,verbose_name="学历要求")
    low_pay = models.IntegerField(verbose_name="最低薪资")
    hig_pay = models.IntegerField(verbose_name="最高薪资")
    info = models.CharField(max_length=200,verbose_name="职位描述")
    Provincial = models.ForeignKey(Provincial,on_delete=models.CASCADE,verbose_name="省") # 省
    city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="市") # 市
    area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name="区/县") # 区
    address = models.CharField(max_length=200,verbose_name="详细地址")
    def __str__(self):
        return self.name

