# Generated by Django 4.0.4 on 2022-04-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_provider_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='start_at',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Start at'),
        ),
    ]
