from django.db import models
from django.contrib.auth.models import AbstractUser

class PjUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=15)
    qq = models.CharField('QQ号', max_length=30)
    wechat = models.CharField('微信号', max_length=40)
    mobile = models.CharField('电话号', max_length=20, unique=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    is_delete = models.BooleanField('是否删除', default=False)

    class Meta:
        db_table = 'UserTable'
