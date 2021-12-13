# Generated by Django 2.2.24 on 2021-12-12 12:45

from django.db import migrations


def fill_owner_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            pure_phone=flat.owner_pure_phone
        )
        if created:
            owner.phonenumber=flat.owners_phonenumber
            owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owner_data),
    ]
