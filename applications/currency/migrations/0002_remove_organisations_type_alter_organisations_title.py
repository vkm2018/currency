# Generated by Django 4.2 on 2023-04-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisations',
            name='type',
        ),
        migrations.AlterField(
            model_name='organisations',
            name='title',
            field=models.TextField(blank=True, choices=[('Bank', 'Bank'), ('Buro', 'Buro')], default='Buro', max_length=100),
        ),
    ]
