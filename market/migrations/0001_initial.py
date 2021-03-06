# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 17:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sku', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('order_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('bill_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_qty', models.IntegerField()),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sale_qty', models.IntegerField()),
                ('sale_value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('door_number', models.CharField(max_length=20)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Community')),
                ('u', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DaysItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_qty', models.IntegerField()),
                ('ordered_loose', models.BooleanField(default=False)),
                ('sold_loose', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Localities',
            },
        ),
        migrations.CreateModel(
            name='LocationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_qty', models.IntegerField()),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deliver_qty', models.IntegerField()),
                ('deliver_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('daysItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.DaysItem')),
            ],
        ),
        migrations.CreateModel(
            name='LocationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Mela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MelaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_qty', models.IntegerField()),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deliver_qty', models.IntegerField()),
                ('deliver_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('daysItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.DaysItem')),
            ],
        ),
        migrations.CreateModel(
            name='MelaLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Mela Locations',
            },
        ),
        migrations.CreateModel(
            name='MelaValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('mela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Mela')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.TextField()),
                ('u', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='locationvalue',
            name='mela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Mela'),
        ),
        migrations.AddField(
            model_name='locationitem',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.MelaLocation'),
        ),
        migrations.AddField(
            model_name='item',
            name='mela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Mela'),
        ),
        migrations.AddField(
            model_name='item',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sku.SKU'),
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sku.Unit'),
        ),
        migrations.AddField(
            model_name='daysitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Item'),
        ),
        migrations.AddField(
            model_name='daysitem',
            name='mela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Mela'),
        ),
        migrations.AddField(
            model_name='community',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Locality'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='daysItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.DaysItem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.MelaLocation'),
        ),
        migrations.AddField(
            model_name='cart',
            name='mela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Mela'),
        ),
    ]
