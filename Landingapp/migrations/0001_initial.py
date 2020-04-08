# Generated by Django 2.2.5 on 2020-02-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
