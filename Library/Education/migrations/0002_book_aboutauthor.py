# Generated by Django 3.0.1 on 2020-01-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='aboutAuthor',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
