# Generated by Django 4.1.5 on 2023-04-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=200)),
                ('project', models.TextField()),
                ('tech', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField(default=18)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]