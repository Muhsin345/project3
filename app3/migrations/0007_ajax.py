# Generated by Django 3.2.8 on 2021-11-13 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0006_up_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ajax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('E_mail', models.CharField(max_length=100)),
            ],
        ),
    ]
