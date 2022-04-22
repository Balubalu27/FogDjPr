# Generated by Django 4.0.4 on 2022-04-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('postal_code', models.IntegerField(verbose_name='postal_code')),
                ('country', models.CharField(max_length=150, verbose_name='country')),
                ('federal_district', models.CharField(max_length=150, verbose_name='federal_district')),
                ('region_type', models.CharField(max_length=100, verbose_name='region_type')),
                ('region', models.CharField(max_length=150, verbose_name='region')),
                ('area_type', models.CharField(max_length=150, verbose_name='area_type')),
                ('area', models.CharField(max_length=150, verbose_name='area')),
                ('city_type', models.CharField(max_length=150, verbose_name='city_type')),
                ('city', models.CharField(max_length=150, verbose_name='city')),
                ('settlement_type', models.CharField(max_length=150, verbose_name='settlement_type')),
                ('settlement', models.CharField(max_length=150, verbose_name='settlement')),
                ('kladr_id', models.IntegerField(verbose_name='kladr_id')),
                ('fias_id', models.CharField(max_length=150, verbose_name='fias_id')),
                ('fias_level', models.IntegerField(verbose_name='fias_level')),
                ('capital_marker', models.IntegerField(verbose_name='capital_marker')),
                ('okato', models.IntegerField(verbose_name='okato')),
                ('oktmo', models.IntegerField(verbose_name='oktmo')),
                ('tax_office', models.IntegerField(verbose_name='tax_office')),
                ('timezone', models.CharField(max_length=150, verbose_name='timezone')),
                ('geo_lat', models.FloatField(verbose_name='geo_lat')),
                ('geo_lon', models.FloatField(verbose_name='geo_lon')),
                ('population', models.IntegerField(verbose_name='population')),
                ('foundation_year', models.IntegerField(verbose_name='foundation_year')),
            ],
        ),
    ]