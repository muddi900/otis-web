# Generated by Django 3.0.3 on 2020-05-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0045_auto_20200429_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='adjustment',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Adjustment to the cost.', max_digits=8),
        ),
    ]