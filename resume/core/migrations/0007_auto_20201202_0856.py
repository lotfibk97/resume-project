# Generated by Django 3.1.2 on 2020-12-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201202_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adresse',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='adresse'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='phone'),
        ),
    ]