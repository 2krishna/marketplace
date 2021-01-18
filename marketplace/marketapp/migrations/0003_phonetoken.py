# Generated by Django 2.2 on 2021-01-16 21:24

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0002_myuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(editable=False, max_length=128)),
                ('otp', models.CharField(editable=False, max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('attempts', models.IntegerField(default=0)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'OTP Token',
                'verbose_name_plural': 'OTP Tokens',
            },
        ),
    ]
