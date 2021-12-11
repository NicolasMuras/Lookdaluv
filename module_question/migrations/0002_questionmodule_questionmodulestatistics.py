# Generated by Django 3.1.7 on 2021-12-11 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0001_initial'),
        ('module_question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModule',
            fields=[
                ('module_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modules.module')),
                ('difficult', models.PositiveSmallIntegerField(choices=[(1, 'Very Easy'), (2, 'Easy'), (3, 'Medium'), (4, 'Hard'), (5, 'Very Hard'), (6, 'Nightmare')], default=3, verbose_name='Difficult')),
                ('level_steps', models.IntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Question Module',
                'verbose_name_plural': 'Question Modules',
            },
            bases=('modules.module',),
        ),
        migrations.CreateModel(
            name='QuestionModuleStatistics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Update Date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deletion Date')),
                ('completed', models.BooleanField(default=False)),
                ('max_step_reached', models.IntegerField(default=1)),
                ('value_generated', models.IntegerField(default=1)),
                ('trap_passed', models.BooleanField(blank=True, default=False)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='module_question.questionmodule', verbose_name='Module')),
            ],
            options={
                'verbose_name': 'Question Statistic',
                'verbose_name_plural': 'Question Statistics',
            },
        ),
    ]
