# Generated by Django 5.0.6 on 2024-06-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoo',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
