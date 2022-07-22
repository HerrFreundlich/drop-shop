# Generated by Django 4.0.6 on 2022-07-22 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.BooleanField(default=False)),
                ('buyer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='buyer_profile.buyerprofilemodel')),
            ],
        ),
    ]
