# Generated by Django 2.0.6 on 2018-06-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0003_auto_20180618_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
