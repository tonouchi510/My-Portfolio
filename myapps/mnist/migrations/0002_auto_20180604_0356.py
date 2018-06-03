# Generated by Django 2.0.5 on 2018-06-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mnist',
            name='data_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mnist',
            name='label',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')]),
        ),
    ]
