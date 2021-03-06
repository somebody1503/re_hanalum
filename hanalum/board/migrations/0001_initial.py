# Generated by Django 3.0.2 on 2020-04-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_id', models.CharField(max_length=100, verbose_name='Board_id')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('auth_read', models.IntegerField(default=0, verbose_name='Auth_read')),
                ('auth_write', models.IntegerField(default=0, verbose_name='Auth_write')),
                ('use_comment', models.BooleanField(default=True, verbose_name='Use_comment')),
                ('use_good', models.BooleanField(default=True, verbose_name='Use_good')),
                ('use_bad', models.BooleanField(default=True, verbose_name='Use_bad')),
                ('use_anony', models.BooleanField(default=False, verbose_name='Use_anony')),
            ],
        ),
    ]
