# Generated by Django 3.2.18 on 2023-02-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
