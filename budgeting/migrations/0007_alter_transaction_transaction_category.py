# Generated by Django 5.0.6 on 2024-06-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0006_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_category',
            field=models.CharField(choices=[('GR', 'Groceries'), ('FD', 'Food Delivery'), ('RS', 'Restaurants'), ('SN', 'Snacks'), ('CO', 'Coffee'), ('AL', 'Alcohol & Bars'), ('HO', 'Home'), ('UT', 'Utilities'), ('RE', 'Rent & Mortgage'), ('ED', 'Education'), ('KI', 'Kids'), ('PE', 'Pets'), ('HE', 'Health'), ('SC', 'Selfcare'), ('MD', 'Medical'), ('SA', 'Savings'), ('CR', 'Charity'), ('CL', 'Clothes'), ('SU', 'Subscriptions'), ('TE', 'Tech'), ('AM', 'Amazon'), ('GI', 'Gifts'), ('EN', 'Entertainment'), ('LO', 'Loans'), ('IV', 'Investments'), ('TX', 'Taxes'), ('P4', 'Pay in 4'), ('BT', 'Betting'), ('CA', 'Car'), ('GA', 'Gas'), ('TP', 'Transportation'), ('TR', 'Travel'), ('UB', 'Uber'), ('WK', 'Work'), ('IN', 'Insurance'), ('RT', 'Retirement'), ('MI', 'Misc'), ('OT', 'Other')], default='MI', max_length=2),
        ),
    ]
