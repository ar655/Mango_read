# Generated by Django 4.1.7 on 2023-03-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_card_genre_alter_genre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
