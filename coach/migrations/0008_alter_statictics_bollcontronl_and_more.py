# Generated by Django 4.1.2 on 2022-11-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0007_statictics_shoot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statictics',
            name='bollcontronl',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='statictics',
            name='passaccuracy',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='statictics',
            name='shoot',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='statictics',
            name='speed',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='statictics',
            name='stamina',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='statictics',
            name='takles',
            field=models.IntegerField(default=50),
        ),
    ]
