# Generated by Django 3.2.2 on 2021-05-10 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='brand',
            new_name='name',
        ),
    ]
