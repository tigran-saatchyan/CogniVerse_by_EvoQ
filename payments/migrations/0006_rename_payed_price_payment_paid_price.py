# Generated by Django 4.2.5 on 2023-09-29 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_payment_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payed_price',
            new_name='paid_price',
        ),
    ]
