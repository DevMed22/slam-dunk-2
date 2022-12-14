# Generated by Django 4.0.7 on 2022-10-01 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=3)),
                ('PAC', models.PositiveSmallIntegerField()),
                ('SHO', models.PositiveSmallIntegerField()),
                ('PAS', models.PositiveSmallIntegerField()),
                ('DRI', models.PositiveSmallIntegerField()),
                ('DEF', models.PositiveSmallIntegerField()),
                ('PHY', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
