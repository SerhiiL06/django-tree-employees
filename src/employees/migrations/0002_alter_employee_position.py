# Generated by Django 4.2 on 2024-04-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('position_1', 'position_1'), ('position_2', 'position_2'), ('position_3', 'position_3'), ('position_4', 'position_4'), ('position_5', 'position_5'), ('position_6', 'position_6'), ('position_7', 'position_7'), ('position_8', 'position_8')], max_length=20),
        ),
    ]