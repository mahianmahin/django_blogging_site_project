# Generated by Django 3.1.7 on 2021-05-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_blog_superuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='superuser_status',
            field=models.BooleanField(null=True),
        ),
    ]