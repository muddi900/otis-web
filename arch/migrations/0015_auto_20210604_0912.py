# Generated by Django 3.1.8 on 2021-06-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch', '0014_remove_problem_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='keywords',
            field=models.CharField(blank=True, default='', help_text="A comma-separated list of keywords that a solver could look at to help them guess whether the hint is relevant or not. These are viewable immediately, so no spoilers here. Examples are 'setup', 'advice', 'answer confirmation', 'nudge', 'main idea', 'solution set', 'converse direction', 'construction', etc. Not all hints go well with keywords, so you can leave this blank if you can't think of anything useful to write.", max_length=255),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.CharField(help_text="A short description of the problem, e.g. 'Quirky triangles.'. Most important if the problem does not have a source given. Use sentence case.", max_length=255),
        ),
        migrations.AlterField(
            model_name='problem',
            name='source',
            field=models.CharField(blank=True, help_text="The source of the problem, such as 'TSTST 2020/3'.If in doubt on formatting, follow what is written on the handout.", max_length=64),
        ),
    ]