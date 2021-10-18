from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32,db_index=True)
    email = models.EmailField(verbose_name='邮箱',max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=32)
    # price_policy = models.ForeignKey(verbose_name='价格策略',to='PricePolicy',null=True,blank=True)

class PricePolicy(models.Model):
    # 价格策略
    category_choices = (
        (1,'免费版'),
        (2,'收费版'),
        (3,'其他'),
    )

    category = models.SmallIntegerField(verbose_name='收费类型',default=2,choices=category_choices)
    title = models.CharField(verbose_name='标题',max_length=32)
    price = models.PositiveIntegerField(verbose_name='价格')

    project_num = models.PositiveIntegerField(verbose_name='项目数')
    project_member = models.PositiveIntegerField(verbose_name='项目成员数')
    project_space = models.PositiveIntegerField(verbose_name='单项目空间')
    per_file_size = models.PositiveIntegerField(verbose_name='单文件大小（M）')

    create_datetime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

class Transaction(models.Model):
    '''交易记录'''
    status_choice = (
        (1,'未支付'),
        (2,'已支付'),
    )

    status = models.SmallIntegerField(verbose_name='状态',choices=status_choice)

    order = models.CharField(verbose_name='订单号',max_length=64,unique=True) # 唯一索引

    user = models.ForeignKey(verbose_name='用户',to='UserInfo')
    price_policy = models.ForeignKey(verbose_name='价格策略',to='PricePolicy',null=True,blank=True)

    count = models.IntegerField(verbose_name='数量（年）',help_text='0表示无限制')

    price = models.IntegerField(verbose_name='实际支付价格')

    start_datetime = models.DateTimeField(verbose_name='开始时间',null=True,blank=True)
    end_datetime = models.DateTimeField(verbose_name='结束时间',null=True,blank=True)

    create_datetime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

class Project(models.Model):
    '''项目表'''
    COLOR_CHOICES = (
        (1,'#A02128'),
        (2,'#D15B8F'),
        (3,'#DD7907'),
        (4,'#D2B773'),
        (5,'#28713E'),
        (6,'#154889'),
        (7,'#8F4E35'),
    )
    name = models.CharField(verbose_name='项目表',max_length=32)
    color = models.SmallIntegerField(verbose_name='颜色',choices=COLOR_CHOICES,default=1)
    desc = models.CharField(verbose_name='项目描述',max_length=255,null=True,blank=True)
    use_space = models.BigIntegerField(verbose_name='项目已使用空间',default=0)
    star = models.BooleanField(verbose_name='星标',default=False)

    bucket = models.CharField(verbose_name='COS桶',max_length=128)
    region = models.CharField(verbose_name='COS区域',max_length=32)

    join_count = models.SmallIntegerField(verbose_name='参与人数',default=1)
    creator = models.ForeignKey(verbose_name='创建者',to='UserInfo')
    create_datetime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

    # 查询，可以省事儿
    # 增加、删除、修改：无法完成
    # project_user = models.ManyToManyField(to='UserInfo',through='ProjectUser',through_fields=('projects','user'))

class ProjectUser(models.Model):
    '''项目参与者'''
    user = models.ForeignKey(verbose_name='参与者',to='UserInfo',related_name='projects')
    projects = models.ForeignKey(verbose_name='项目',to='Project')

    invitee = models.ForeignKey(verbose_name='邀请者',to='UserInfo',related_name='invites',null=True,blank=True)

    star = models.BooleanField(verbose_name='星标',default=True)

    create_time = models.DateTimeField(verbose_name='加入时间',auto_now_add=True)


class Wiki(models.Model):
    project = models.ForeignKey(verbose_name='项目',to='Project')
    title = models.CharField(verbose_name='标题',max_length=32)
    content = models.TextField(verbose_name='内容')
    depth = models.IntegerField(verbose_name='深度',default=1)
    # 自关联
    parent = models.ForeignKey(verbose_name='父文章',to='Wiki',null=True,blank=True,related_name='children')

    def __str__(self):
        return self.title



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline