# Generated by Django 3.0.6 on 2020-08-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(blank=True, max_length=5000, null=True, verbose_name='作者')),
                ('content', models.TextField(max_length=5000, verbose_name='内容')),
                ('date', models.TextField(max_length=100, verbose_name='日期')),
                ('entities', models.TextField(max_length=5000, verbose_name='实体')),
                ('title', models.TextField(max_length=5000, verbose_name='题目')),
                ('type', models.CharField(max_length=100, verbose_name='种类标签')),
            ],
            options={
                'verbose_name': '整合数据信息',
                'verbose_name_plural': '整合数据信息',
            },
        ),
        migrations.DeleteModel(
            name='news',
        ),
        migrations.DeleteModel(
            name='research_papers',
        ),
        migrations.DeleteModel(
            name='rumors',
        ),
    ]
