# Generated by Django 3.2.15 on 2022-09-18 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_orderitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='ToppingItem',
        ),
        migrations.RenameField(
            model_name='toppingitem',
            old_name='base_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='toppingitem',
            old_name='toppings',
            new_name='name',
        ),
    ]
