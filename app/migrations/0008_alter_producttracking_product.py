# Generated by Django 5.0.4 on 2024-04-28 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_producttracking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttracking',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
