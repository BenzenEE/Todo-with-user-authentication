# Generated by Django 4.0.2 on 2022-04-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0016_remove_test_id_alter_test_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tlist',
            name='status',
            field=models.CharField(default='Pending', max_length=15),
        ),
    ]
