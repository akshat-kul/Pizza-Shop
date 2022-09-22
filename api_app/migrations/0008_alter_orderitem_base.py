# Generated by Django 3.2.15 on 2022-09-18 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_rename_base_id_orderitem_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_id', to='api_app.pizzaitem'),
        ),
    ]
