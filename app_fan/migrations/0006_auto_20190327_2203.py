# Generated by Django 2.1.7 on 2019-03-27 14:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190321_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyregistry',
            name='CorporateContactNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='processorregistry',
            name='companyregistry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processor', to='app.CompanyRegistry'),
        ),
        migrations.AddField(
            model_name='processorregistry',
            name='imgID',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='processorregistry',
            name='imgquality',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='processorregistry',
            name='imgwork',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='quarantineregistry',
            name='companyregistry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarantine', to='app.CompanyRegistry'),
        ),
        migrations.AddField(
            model_name='quarantineregistry',
            name='imgID',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='quarantineregistry',
            name='imgquality1',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='quarantineregistry',
            name='imgquality2',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='quarantineregistry',
            name='imgwork',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='sellerregistry',
            name='companyregistry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='app.CompanyRegistry'),
        ),
        migrations.AddField(
            model_name='sellerregistry',
            name='imgID',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='sellerregistry',
            name='imgwork',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='transporterregistry',
            name='companyregistry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transporter', to='app.CompanyRegistry'),
        ),
        migrations.AddField(
            model_name='transporterregistry',
            name='imgID',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='transporterregistry',
            name='imgquality',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='transporterregistry',
            name='imgwork',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='AEPCertificateNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='AnimalEpidemicPCNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='BLicenseDeadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='BLicenseRegisterNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='CorporateIDNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='FoodDistributionLicenseNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='FoodHygienePermitNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='InvestigateRes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='OperatingKind',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='OrganizationCodeCertificateNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='PLicenseDeadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='RoadTransportBusinessLicenseNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='companyregistry',
            name='TaxRCNo',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='companyregistry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producer', to='app.CompanyRegistry'),
        ),
    ]
