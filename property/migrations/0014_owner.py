# Generated by Django 2.2.24 on 2021-12-12 09:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20211211_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
