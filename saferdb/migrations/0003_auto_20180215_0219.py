# Generated by Django 2.0 on 2018-02-15 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saferdb', '0002_auto_20180215_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Physical_adress',
            new_name='adress',
        ),
    ]
