# Generated by Django 3.2.6 on 2021-08-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
