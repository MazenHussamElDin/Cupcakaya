# Generated by Django 4.2 on 2023-05-15 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0009_coverage_image_option_image_toppings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='amount',
            field=models.CharField(max_length=100),
        ),
    ]