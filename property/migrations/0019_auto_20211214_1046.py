# Generated by Django 2.2.24 on 2021-12-14 07:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20211213_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='address',
            field=models.TextField(db_index=True, help_text='ул. Подольских курсантов д.5 кв.4', verbose_name='Адрес квартиры'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.CharField(db_index=True, help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town_district',
            field=models.CharField(blank=True, db_index=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район города, где находится квартира'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
