# Generated by Django 2.1.5 on 2020-10-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
    ]