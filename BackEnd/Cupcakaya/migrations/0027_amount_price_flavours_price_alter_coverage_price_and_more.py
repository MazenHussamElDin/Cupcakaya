# Generated by Django 4.2 on 2023-05-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0026_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='flavours',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='coverage',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='shape',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]