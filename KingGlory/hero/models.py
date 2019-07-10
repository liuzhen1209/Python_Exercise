from django.db import models


# Create your models here.
class GloryPracice(models.Model):
    """英雄概览"""
    name = models.CharField(max_length=20)  # 英雄名
    dialogue = models.CharField(max_length=100)  # 台词
    age = models.IntegerField()  # 年龄
    sex = models.BooleanField()  # 性别
    glory_type = models.CharField(max_length=10)  # 英雄职业

    def __str__(self):
        return "英雄表"


class GlorySkill(models.Model):
    """技能表"""
    skill_name = models.CharField(max_length=20)    # 技能名
    skill_type = models.CharField(max_length=20)    # 技能类型 主动被动大招
    skill_desc = models.CharField(max_length=1000)  # 技能描述
    glory = models.ForeignKey('GloryPracice')       # 关联英雄对象

    def __str__(self):
        return "技能表"

