# Generated by Django 3.2.5 on 2021-08-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_semester_uses_legacy_pset_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='uses_legacy_pset_system',
            field=models.BooleanField(default=False, help_text='Whether the pset uses the old system of upload checking'),
        ),
    ]