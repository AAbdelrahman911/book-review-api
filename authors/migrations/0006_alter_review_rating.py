# Generated by Django 5.1.4 on 2025-01-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
