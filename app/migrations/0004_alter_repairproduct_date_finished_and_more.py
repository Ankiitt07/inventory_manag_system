# Generated by Django 5.0.4 on 2024-04-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_repairproduct_date_finished_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairproduct',
            name='date_finished',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repairproduct',
            name='date_started',
            field=models.DateField(blank=True, null=True),
        ),
    ]
