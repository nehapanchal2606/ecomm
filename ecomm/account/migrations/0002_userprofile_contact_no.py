# Generated by Django 4.1.4 on 2022-12-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact_no',
            field=models.CharField(default=-1, max_length=13, verbose_name='Contact Number'),
            preserve_default=False,
        ),
    ]
