# Generated by Django 3.1.7 on 2021-05-31 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210531_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='superuser_status',
            field=models.BooleanField(null=True),
        ),
    ]
