# Generated by Django 3.1 on 2021-04-07 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
