# Generated by Django 2.2.24 on 2021-12-11 07:05

from django.db import migrations

def fill_new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.new_building is None:
            if flat.construction_year >= 2015:
                flat.new_building = True
            else:
                flat.new_building = False
            flat.save()
        

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_buildings),
    ]
