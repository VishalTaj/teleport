# Generated by Django 3.2.4 on 2021-06-15 07:09

from django.db import migrations, transaction
from django.template.defaultfilters import slugify
import json
from pathlib import Path


DATA_FILENAME = 'fixtures/city.json'
def load_data(apps, schema_editor):
    City = apps.get_model('weather_finder', 'City')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME
    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects:
            try:
                with transaction.atomic():
                    title = obj.get('name')
                    coord = obj['coord']
                    lat = coord.get('lat')
                    lon = coord.get('lon')
                    slug = slugify(title)
                    City(title=title, latitutde=lat, longitude=lon, slug=slug).save()
            except:
                pass
            
        
    




       

class Migration(migrations.Migration):

    dependencies = [
        ('weather_finder', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
