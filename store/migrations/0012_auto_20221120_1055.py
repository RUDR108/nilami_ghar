# Generated by Django 3.1 on 2022-11-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20221120_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]