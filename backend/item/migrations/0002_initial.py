# Generated by Django 4.0.6 on 2022-07-21 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('seller_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='seller_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='seller_profile.sellerprofilemodel'),
        ),
    ]
