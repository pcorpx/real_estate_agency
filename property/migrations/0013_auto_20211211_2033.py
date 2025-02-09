# Generated by Django 2.2.24 on 2021-12-11 17:33

from django.db import migrations

import phonenumbers

def normalize_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            ru_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(ru_number):
                flat.owner_pure_phone = (
                    f'+{ru_number.country_code}{ru_number.national_number}'
                )
            else:
                flat.owner_pure_phone = None
        except:
            flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20211211_2017'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber),
    ]
