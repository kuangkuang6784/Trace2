# Generated by Django 2.1.7 on 2019-03-02 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Product', models.CharField(max_length=99)),
                ('weight', models.FloatField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('part', models.CharField(max_length=15)),
                ('ID_Sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Total.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('location', models.CharField(max_length=50)),
                ('delivery', models.CharField(max_length=15)),
                ('ID_Transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Total.Product')),
            ],
        ),
    ]
