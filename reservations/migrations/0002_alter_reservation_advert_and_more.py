# Generated by Django 4.1.5 on 2023-01-10 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_alter_advert_platform_tax'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='advert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adverts.advert', verbose_name='Advert'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkin_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Checkin date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Checkout date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(max_length=20, unique=True, verbose_name='Reservation code'),
        ),
    ]
