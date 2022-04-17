# Generated by Django 4.0.4 on 2022-04-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filename', models.CharField(max_length=1000)),
                ('FileOwner', models.CharField(max_length=50)),
                ('UploadDate', models.DateTimeField(verbose_name='date uploaded')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('PersonalToken', models.CharField(max_length=200)),
            ],
        ),
    ]
