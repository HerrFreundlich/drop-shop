# Generated by Django 4.0.6 on 2022-07-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller_profile', '0001_initial'),
        ('column', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='columnmodel',
            name='seller_profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='seller_profile.sellerprofilemodel'),
        ),
    ]
