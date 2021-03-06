# Generated by Django 4.0.4 on 2022-04-27 08:47

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Product.category', verbose_name='Parent')),
            ],
        ),
        migrations.CreateModel(
            name='DataAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=200, verbose_name='Attribute')),
                ('description', models.TextField(verbose_name='Description')),
                ('example', models.TextField(verbose_name='Example')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=200, verbose_name='Format')),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(max_length=200, verbose_name='Frequency')),
            ],
        ),
        migrations.CreateModel(
            name='Methods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=200, verbose_name='Method')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=200, verbose_name='License')),
                ('start_at', models.CharField(max_length=200, verbose_name='Start at')),
            ],
        ),
        migrations.CreateModel(
            name='SuitableCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_size', models.CharField(max_length=200, verbose_name='Company size')),
            ],
        ),
        migrations.CreateModel(
            name='UseCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_cases', models.CharField(max_length=200, verbose_name='Use Cases')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='Number')),
                ('content', models.CharField(max_length=200, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('history', models.CharField(max_length=200, verbose_name='History')),
                ('icon', models.ImageField(upload_to='Product/icon', verbose_name='Icon')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('category', models.ManyToManyField(to='Product.category', verbose_name='Category')),
                ('data_attribute', models.ManyToManyField(to='Product.dataattribute', verbose_name='Data Attribute')),
                ('format', models.ManyToManyField(to='Product.format', verbose_name='Format')),
                ('frequency', models.ManyToManyField(to='Product.frequency', verbose_name='Frequency')),
                ('methods', models.ManyToManyField(to='Product.methods', verbose_name='Methods')),
                ('pricing', models.ManyToManyField(to='Product.pricing', verbose_name='Pricing')),
                ('suitable_company', models.ManyToManyField(to='Product.suitablecompany', verbose_name='Suitable company size')),
                ('use_cases', models.ManyToManyField(to='Product.usecases', verbose_name='Use Cases')),
                ('volume', models.ManyToManyField(to='Product.volume', verbose_name='Volume')),
            ],
        ),
    ]
