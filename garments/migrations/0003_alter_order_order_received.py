# Generated by Django 3.2.4 on 2021-08-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garments', '0002_auto_20210802_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_received',
            field=models.DateField(),
        ),
    ]