# Generated by Django 4.0.7 on 2022-10-01 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_card_def_alter_card_dri_alter_card_pac_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]