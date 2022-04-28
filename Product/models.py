from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class Product(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')
    history = models.CharField('History', max_length=200)
    icon = models.ImageField('Icon', upload_to='Product/Icon')
    country = CountryField(multiple=True)
    use_cases = models.ManyToManyField('UseCases', verbose_name="Use Cases")
    category = models.ManyToManyField('Category', verbose_name='Category')
    suitable_company = models.ManyToManyField('SuitableCompany', verbose_name="Suitable company size")
    methods = models.ManyToManyField('Methods', verbose_name="Methods")
    data_attribute = models.ManyToManyField('DataAttribute', verbose_name='Data Attribute')
    frequency = models.ManyToManyField('Frequency', verbose_name="Frequency")
    format = models.ManyToManyField('Format', verbose_name="Format")
    volume = models.ManyToManyField('Volume', verbose_name='Volume')
    pricing = models.ManyToManyField('Pricing', verbose_name='Pricing')
    provider = models.ForeignKey('Provider', verbose_name='Provider', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Name", max_length=200)
    parent = models.ForeignKey('Category', verbose_name='Parent', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"{self.parent.name} ==> {self.name}" if self.parent else f"{self.name}"


class Methods(models.Model):
    method = models.CharField('Method', max_length=200)

    def __str__(self):
        return self.method


class SuitableCompany(models.Model):
    company_size = models.CharField('Company size', max_length=200)

    def __str__(self):
        return self.company_size


class UseCases(models.Model):
    use_cases = models.CharField('Use Cases', max_length=200)

    def __str__(self):
        return self.use_cases


class DataAttribute(models.Model):
    attribute = models.CharField('Attribute', max_length=200)
    description = models.TextField('Description')
    example = models.TextField('Example')

    def __str__(self):
        return self.attribute


class Frequency(models.Model):
    frequency = models.CharField('Frequency', max_length=200)

    def __str__(self):
        return self.frequency


class Format(models.Model):
    format = models.CharField('Format', max_length=200)

    def __str__(self):
        return self.format


class Volume(models.Model):
    number = models.CharField('Number', max_length=200)
    content = models.CharField('Content', max_length=200)

    def __str__(self):
        return self.content


class Pricing(models.Model):
    license = models.CharField('License', max_length=200)
    start_at = models.CharField('Start at', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.license


class Provider(models.Model):
    name = models.CharField('Name', max_length=200)
    description = models.TextField('Description')
    icon = models.ImageField('Icon', upload_to='Provider/Icon')
    rate = models.PositiveIntegerField('Rate', null=True, blank=True)
    verified = models.BooleanField("Verified")
    manager_name = models.CharField('Manager name', max_length=100, null=True, blank=True)
    manager_img = models.ImageField('Manager image', upload_to='Provider/ManagerImage', null=True, blank=True)

    def __str__(self):
        return self.name
