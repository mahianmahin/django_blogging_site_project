# Generated by Django 3.1.7 on 2021-05-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210531_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='superuser_status',
            field=models.BooleanField(null=True),
        ),
    ]