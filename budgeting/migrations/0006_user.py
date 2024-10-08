# Generated by Django 5.0.6 on 2024-06-12 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0005_alter_transaction_transaction_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('is_logged_in', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
                ('access_token', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
