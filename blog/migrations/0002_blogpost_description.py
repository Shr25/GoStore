# Generated by Django 3.2.4 on 2021-06-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
