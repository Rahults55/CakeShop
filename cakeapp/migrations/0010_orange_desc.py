# Generated by Django 3.2.16 on 2022-12-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0009_orange_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orange',
            name='desc',
            field=models.TextField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
