# Generated by Django 4.2.6 on 2023-10-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silant', '0003_alter_to_data_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date_refusal',
            field=models.DateField(),
        ),
    ]
