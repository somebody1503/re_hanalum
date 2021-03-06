# Generated by Django 3.0.2 on 2020-04-14 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=20, verbose_name='Menu_name')),
                ('menu_url', models.URLField(blank=True, null=True, verbose_name='Menu_url')),
                ('menu_authority', models.IntegerField(default=0, verbose_name='Menu_authority')),
                ('menu_sort', models.IntegerField(default=0, verbose_name='Menu_sort')),
            ],
        ),
        migrations.CreateModel(
            name='Sidebar_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=20, verbose_name='Menu_name')),
                ('menu_url', models.URLField(blank=True, null=True, verbose_name='Menu_url')),
                ('menu_authority', models.IntegerField(default=0, verbose_name='Menu_authority')),
                ('menu_sort', models.IntegerField(default=0, verbose_name='Menu_sort')),
                ('upper_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Sidebar_category')),
            ],
        ),
    ]
