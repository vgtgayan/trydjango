# Generated by Django 2.0.7 on 2020-10-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='This is a sample Product'),
        ),
    ]