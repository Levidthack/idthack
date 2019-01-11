# Generated by Django 2.0 on 2018-01-31 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('DOT_Number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Entity_Type', models.CharField(max_length=200)),
                ('Operating_Status', models.CharField(max_length=200)),
                ('Legal_Name', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=200)),
                ('Units', models.CharField(max_length=10)),
                ('Drivers', models.CharField(max_length=10)),
                ('Mileage', models.CharField(max_length=200)),
                ('For_Hire', models.CharField(max_length=200)),
                ('Exempt_For_Hire', models.CharField(max_length=200)),
                ('Private_Property', models.CharField(max_length=200)),
                ('Priv_Pass', models.CharField(max_length=200)),
                ('Priv_Pass_Non', models.CharField(max_length=200)),
                ('Migrant', models.CharField(max_length=200)),
                ('Fed_Gov', models.CharField(max_length=200)),
                ('State_Gov', models.CharField(max_length=200)),
                ('Local_Gov', models.CharField(max_length=200)),
                ('Indian_Nation', models.CharField(max_length=200)),
                ('Interstate', models.CharField(max_length=200)),
                ('Intrastate_Only_HM', models.CharField(max_length=200)),
                ('Intrastate_NonHM', models.CharField(max_length=200)),
                ('General_Freight', models.CharField(max_length=200)),
                ('Household_Goods', models.CharField(max_length=200)),
                ('Metal_sheets_coils_rolls', models.CharField(max_length=200)),
                ('Motor_Vehicles', models.CharField(max_length=200)),
                ('DriveTow_away', models.CharField(max_length=200)),
                ('Logs_Poles_Beams_Lumber', models.CharField(max_length=200)),
                ('Building_Materials', models.CharField(max_length=200)),
                ('Mobile_Homes', models.CharField(max_length=200)),
                ('Machinery_Large_Objects', models.CharField(max_length=200)),
                ('Fresh_Produce', models.CharField(max_length=200)),
                ('LiquidsGases', models.CharField(max_length=200)),
                ('Intermodal_Cont', models.CharField(max_length=200)),
                ('Passengers', models.CharField(max_length=200)),
                ('Oilfield_Equipment', models.CharField(max_length=200)),
                ('Livestock', models.CharField(max_length=200)),
                ('Grain_Feed_Hay', models.CharField(max_length=200)),
                ('CoalCoke', models.CharField(max_length=200)),
                ('Meat', models.CharField(max_length=200)),
                ('GarbageRefuse', models.CharField(max_length=200)),
                ('US_Mail', models.CharField(max_length=200)),
                ('Chemicals', models.CharField(max_length=200)),
                ('Commodities_Dry_Bulk', models.CharField(max_length=200)),
                ('Refrigerated_Food', models.CharField(max_length=200)),
                ('Beverages', models.CharField(max_length=200)),
                ('Paper_Products', models.CharField(max_length=200)),
                ('Utilities', models.CharField(max_length=200)),
                ('AgriculturalFarm_Supplies', models.CharField(max_length=200)),
                ('Construction', models.CharField(max_length=200)),
                ('Water_Well', models.CharField(max_length=200)),
            ],
        ),
    ]