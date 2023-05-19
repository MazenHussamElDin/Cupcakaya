# Generated by Django 4.2 on 2023-05-15 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0004_remove_item_amount_remove_item_coverage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.ManyToManyField(to='Cupcakaya.amount'),
        ),
        migrations.AlterField(
            model_name='item',
            name='coverage',
            field=models.ManyToManyField(to='Cupcakaya.coverage'),
        ),
        migrations.AlterField(
            model_name='item',
            name='flavour',
            field=models.ManyToManyField(to='Cupcakaya.flavours'),
        ),
        migrations.AlterField(
            model_name='item',
            name='option',
            field=models.ManyToManyField(to='Cupcakaya.option'),
        ),
        migrations.AlterField(
            model_name='item',
            name='topping',
            field=models.ManyToManyField(to='Cupcakaya.toppings'),
        ),
    ]