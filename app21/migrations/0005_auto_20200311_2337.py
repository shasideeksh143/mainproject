# Generated by Django 3.0.2 on 2020-03-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app21', '0004_auto_20200311_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
