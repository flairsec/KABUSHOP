# Generated by Django 3.2.7 on 2023-01-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
