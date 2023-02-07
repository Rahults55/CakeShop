# Generated by Django 3.2.16 on 2022-12-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0007_apple_banana_blueberry_mango_strawberry'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_say',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='picture')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]