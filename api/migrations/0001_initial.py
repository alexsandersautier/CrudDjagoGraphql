# Generated by Django 5.0.6 on 2024-05-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('year_published', models.CharField(max_length=10)),
                ('review', models.PositiveIntegerField()),
            ],
        ),
    ]
