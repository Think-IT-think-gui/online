# Generated by Django 3.2.3 on 2022-08-24 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0012_alter_signup_info_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Delivery_method',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='Rate',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
