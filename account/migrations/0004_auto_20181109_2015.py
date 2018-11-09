# Generated by Django 2.1.2 on 2018-11-09 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0003_userinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='aboutme',
            field=models.TextField(blank=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='company',
            field=models.CharField(blank=True, max_length=100, verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profession',
            field=models.CharField(blank=True, max_length=100, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.CharField(blank=True, max_length=100, verbose_name='学校'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                       verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                       verbose_name='用户'),
        ),
    ]
