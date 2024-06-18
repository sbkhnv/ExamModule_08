from django.db import models

class users(models.Model):
    full_name = models.CharField(verbose_name="full name",max_length=200,null=True,blank=False)
    user_name = models.CharField(verbose_name="user name",max_length=200,null=True,unique=True)
    telegram_id = models.IntegerField(verbose_name="telegram id",null=False,unique=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user_name


class Furni(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="nomi",max_length=34)
    photo = models.CharField(verbose_name="rasm ",max_length=30,null=True,blank=True)
    price = models.IntegerField(verbose_name="narxi",null=False)
    description = models.TextField(verbose_name="tavsif",null=True,blank=True)

    category_code = models.IntegerField(verbose_name="category_code",null=False)
    category_name = models.CharField(verbose_name="category_name",max_length=34,null=False)
    subcategory_code = models.IntegerField(verbose_name="subcategory_code",null=False)
    subcategory_name = models.CharField(verbose_name="subcategory_name",max_length=34,null=False)

    def __str__(self):
        return self.productname