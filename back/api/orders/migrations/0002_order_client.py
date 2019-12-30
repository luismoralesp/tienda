# Generated by Django 3.0.1 on 2019-12-30 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='orders.Client'),
            preserve_default=False,
        ),
    ]
