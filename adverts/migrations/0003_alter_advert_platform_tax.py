# Generated by Django 4.1.5 on 2023-01-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_alter_advert_platform_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='platform_tax',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Platform tax'),
        ),
    ]
