# Generated by Django 4.2 on 2023-05-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cupcakaya', '0011_shape'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavours',
            name='category',
            field=models.CharField(choices=[('Ck', 'Cake'), ('Cup', 'Cupcake'), ('Cp', 'Cakepop'), ('Co', 'Cookie')], max_length=100, null=True),
        ),
    ]
