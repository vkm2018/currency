# Generated by Django 4.2 on 2023-04-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_organisations_type_alter_organisations_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisations',
            name='adress',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='number_phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]