# Generated by Django 3.0.8 on 2020-11-04 12:36

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_last_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[user.models.check_userid]),
        ),
    ]
