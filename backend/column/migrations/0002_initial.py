# Generated by Django 4.0.6 on 2022-07-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('column', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='columnmodel',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='columns', to='item.itemmodel'),
        ),
    ]
