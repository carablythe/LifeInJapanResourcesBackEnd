# Generated by Django 4.0.3 on 2022-03-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='subcategory',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.CharField(max_length=32),
        ),
    ]
