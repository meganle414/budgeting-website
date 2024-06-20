import datetime

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Transaction(models.Model):
    transaction_text = models.CharField(max_length=200)
    transaction_amount = models.FloatField(default=0)
    # i want to keep this so we can have a streak for no spending
    pub_date = models.DateTimeField("date published")

    class Category(models.TextChoices):
        # food
        GROCERIES = 'GR', _('Groceries')
        FOODDELIVERY = 'FD', _('Food Delivery')
        RESTAURANTS = 'RS', _('Restaurants')
        SNACKS = 'SN', _('Snacks')
        COFFEE = 'CO', _('Coffee')
        ALCOHOL = 'AL', _('Alcohol & Bars')

        # home
        HOME = 'HO', _('Home')
        UTILITIES = 'UT', _('Utilities')
        RENT = 'RE', _('Rent & Mortgage')

        # personal
        EDUCATION = 'ED', _('Education')
        KIDS = 'KI', _('Kids')
        PETS = 'PE', _('Pets')
        HEALTH = 'HE', _('Health')
        SELFCARE = 'SC', _('Selfcare')
        MEDICAL = 'MD', _('Medical')
        SAVINGS = 'SA', _('Savings')
        CHARITY = 'CR', _('Charity')

        # shopping
        CLOTHES = 'CL', _('Clothes')
        SUBSCRIPTIONS = 'SU', _('Subscriptions')
        TECH = 'TE', _('Tech')
        AMAZON = 'AM', _('Amazon')
        GIFTS = 'GI', _('Gifts')
        ENTERTAINMENT = 'EN', _('Entertainment')

        # money
        LOANS = 'LO', _('Loans')
        INVESTMENTS = 'IV', _('Investments')
        TAXES = 'TX', _('Taxes')
        PAYIN4 = 'P4', _('Pay in 4')
        BETTING = 'BT', _('Betting')

        # vehicles
        CAR = 'CA', _('Car')
        GAS = 'GA', _('Gas')
        # TRANSPORTATION = 'TP', _('Transportation')
        TRAVEL = 'TR', _('Travel')
        UBER = 'UB', _('Uber')

        # work
        WORK = 'WK', _('Work')
        INSURANCE = 'IN', _('Insurance')
        RETIREMENT = 'RT', _('Retirement')

        # other
        MISCELLANEOUS = 'MI', _('Misc')
        OTHER = 'OT', _('Other')

    # use something similar kind of to put transactions you used to put in the same category as previous sorts
    # def is_upperclass(self):
    #     return self.year_in_school in {
    #         self.YearInSchool.JUNIOR,
    #         self.YearInSchool.SENIOR,
    #     }

    transaction_category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.MISCELLANEOUS,
    )

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def save(self, *args, **kwargs):
        self.transaction_amount = round(self.transaction_amount, 2)
        super(Transaction, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.transaction_text
    
class User(models.Model):
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    is_logged_in = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=500, null=True, blank=True)
    access_token = models.CharField(
        max_length=500, null=True, blank=True)

    def __str__(self):
        return self.email