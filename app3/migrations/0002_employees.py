# Generated by Django 3.2.8 on 2021-10-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
    ]
