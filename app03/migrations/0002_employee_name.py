# Generated by Django 4.2.18 on 2025-01-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Name',
            field=models.CharField(default='Rohan', max_length=50),
            preserve_default=False,
        ),
    ]
