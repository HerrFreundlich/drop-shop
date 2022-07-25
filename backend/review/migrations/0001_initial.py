# Generated by Django 4.0.6 on 2022-07-25 15:17

from django.db import migrations, models
import django.db.models.deletion
import review.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('buyer_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('buyer_profile', models.ForeignKey(blank=True, on_delete=models.SET(review.models.get_sentinel_user), related_name='reviews', to='buyer_profile.buyerprofilemodel')),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='item.itemmodel')),
            ],
        ),
    ]
