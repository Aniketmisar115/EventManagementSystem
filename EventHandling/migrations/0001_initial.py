# Generated by Django 4.0.4 on 2022-05-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventHandling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organiser', models.CharField(max_length=50)),
                ('special_guest', models.CharField(max_length=80)),
                ('date', models.DateTimeField(default=10)),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
    ]
