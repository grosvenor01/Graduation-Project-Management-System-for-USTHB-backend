# Generated by Django 4.1.7 on 2023-05-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0014_validated_themes_note1_validated_themes_note2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='validated_themes',
            name='moy',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
