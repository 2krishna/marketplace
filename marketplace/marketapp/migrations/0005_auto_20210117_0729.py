# Generated by Django 2.2 on 2021-01-17 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0004_auto_20210117_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('otp', models.CharField(blank=True, max_length=250, null=True)),
                ('generate_time', models.DateTimeField(default=datetime.datetime.now)),
                ('is_expired', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='PhoneToken',
        ),
    ]
