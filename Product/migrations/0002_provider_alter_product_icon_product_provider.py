# Generated by Django 4.0.4 on 2022-04-27 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('icon', models.ImageField(upload_to='Provider/Icon', verbose_name='Icon')),
                ('verified', models.BooleanField(verbose_name='Verified')),
                ('manager_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Manager name')),
                ('manager_img', models.ImageField(blank=True, null=True, upload_to='Provider/ManagerImage', verbose_name='Manager image')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='Product/Icon', verbose_name='Icon'),
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.provider', verbose_name='Provider'),
        ),
    ]
