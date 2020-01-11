# Generated by Django 3.0.1 on 2020-01-10 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=222)),
                ('total', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='USD order total')),
                ('emailAdderss', models.EmailField(blank=True, max_length=222, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=222)),
                ('billingAddress1', models.CharField(blank=True, max_length=222)),
                ('billingCity', models.CharField(blank=True, max_length=222)),
                ('billingPostCode', models.CharField(blank=True, max_length=222)),
                ('billingCountry', models.CharField(blank=True, max_length=222)),
                ('shippingName', models.CharField(blank=True, max_length=222)),
                ('shippingAddress1', models.CharField(blank=True, max_length=222)),
                ('shippingCity', models.CharField(blank=True, max_length=222)),
                ('shippingPostCode', models.CharField(blank=True, max_length=222)),
                ('shippingCountry', models.CharField(blank=True, max_length=222)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=222)),
                ('quentity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='USD price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]