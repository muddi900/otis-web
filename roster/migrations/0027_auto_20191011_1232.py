# Generated by Django 2.1.7 on 2019-10-11 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0026_auto_20191011_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unitinquiry',
            options={'ordering': ('-created_at',)},
        ),
    ]