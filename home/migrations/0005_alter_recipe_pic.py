# Generated by Django 3.2.23 on 2024-05-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(upload_to='images'),
        ),
    ]
