# Generated by Django 5.1.3 on 2025-02-10 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_review_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
