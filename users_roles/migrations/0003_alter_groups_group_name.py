# Generated by Django 3.2.3 on 2021-09-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_roles', '0002_alter_profile_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='group_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
