# Generated by Django 4.2.5 on 2023-09-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('card', 'Card'), ('transfer_to_account', 'Transfer to account')], max_length=50, null=True),
        ),
    ]
