# Generated by Django 4.0.5 on 2022-06-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_sec_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sec',
            name='room_number',
            field=models.CharField(max_length=50),
        ),
    ]
