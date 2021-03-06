# Generated by Django 3.1.3 on 2020-11-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(max_length=1000)),
                ('discount_price', models.FloatField(default=0)),
                ('category', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]
