# Generated by Django 2.1.2 on 2018-11-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_daraja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]