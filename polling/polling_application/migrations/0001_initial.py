# Generated by Django 3.2.16 on 2024-01-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logindetails',
            fields=[
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
