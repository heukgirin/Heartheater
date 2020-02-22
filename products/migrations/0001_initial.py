# Generated by Django 2.0.13 on 2020-02-15 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('name_model', models.CharField(blank=True, max_length=20, null=True)),
                ('name_kor', models.CharField(max_length=50)),
                ('name_eng', models.CharField(max_length=50)),
                ('price_sale', models.IntegerField(default=0)),
                ('price_order', models.IntegerField(default=0)),
                ('delivery_price', models.IntegerField(default=0)),
                ('delivery_send', models.CharField(max_length=100)),
                ('delivery_return', models.CharField(max_length=100)),
                ('company_make', models.CharField(max_length=20)),
                ('company_sale', models.CharField(max_length=20)),
                ('company_as', models.CharField(max_length=20)),
                ('inform', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Attr')),
            ],
        ),
    ]
