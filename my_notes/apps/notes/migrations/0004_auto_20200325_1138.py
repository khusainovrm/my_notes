# Generated by Django 3.0.4 on 2020-03-25 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('-date_created',)},
        ),
    ]