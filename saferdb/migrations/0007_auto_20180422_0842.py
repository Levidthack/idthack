# Generated by Django 2.0 on 2018-04-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saferdb', '0006_auto_20180221_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='AgriculturalFarm_Supplies',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Auth_For_Hire',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Beverages',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Building_Materials',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Chemicals',
        ),
        migrations.RemoveField(
            model_name='question',
            name='City',
        ),
        migrations.RemoveField(
            model_name='question',
            name='CoalCoke',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Commodities_Dry_Bulk',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Construction',
        ),
        migrations.RemoveField(
            model_name='question',
            name='DBA_Name',
        ),
        migrations.RemoveField(
            model_name='question',
            name='DOT_Number',
        ),
        migrations.RemoveField(
            model_name='question',
            name='DUNSNumber',
        ),
        migrations.RemoveField(
            model_name='question',
            name='DriveTow_away',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Drivers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Entity_Type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Exempt_For_Hire',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Fed_Gov',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Fresh_Produce',
        ),
        migrations.RemoveField(
            model_name='question',
            name='GarbageRefuse',
        ),
        migrations.RemoveField(
            model_name='question',
            name='General_Freight',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Grain_Feed_Hay',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Granite',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Household_Goods',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Indian_Nation',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Intermodal_Cont',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Interstate',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Intrastate_NonHM',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Intrastate_Only_HM',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Legal_Name',
        ),
        migrations.RemoveField(
            model_name='question',
            name='LiquidsGases',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Livestock',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Local_Gov',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Logs_Poles_Beams_Lumber',
        ),
        migrations.RemoveField(
            model_name='question',
            name='MCMXFFNumber',
        ),
        migrations.RemoveField(
            model_name='question',
            name='MCS150',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Machinery_Large_Objects',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Mailing_Address',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Meat',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Metal_sheets_coils_rolls',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Migrant',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Mileage',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Mobile_Homes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Motor_Vehicles',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Oilfield_Equipment',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Operating_Status',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Out_Of_Service_Date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Paper_Products',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Passengers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Physical_adress',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Priv_Pass_Business',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Priv_Pass_Non_Business',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Private_Property',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Refrigerated_Food',
        ),
        migrations.RemoveField(
            model_name='question',
            name='State',
        ),
        migrations.RemoveField(
            model_name='question',
            name='StateCarrierIDNumber',
        ),
        migrations.RemoveField(
            model_name='question',
            name='State_Gov',
        ),
        migrations.RemoveField(
            model_name='question',
            name='US_Mail',
        ),
        migrations.RemoveField(
            model_name='question',
            name='US_Mail_Cargo',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Units',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Utilities',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Water_Well',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ZipCode',
        ),
        migrations.RemoveField(
            model_name='question',
            name='mCity',
        ),
        migrations.RemoveField(
            model_name='question',
            name='mState',
        ),
        migrations.RemoveField(
            model_name='question',
            name='mZipCode',
        ),
        migrations.AddField(
            model_name='question',
            name='cardFound',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='question',
            name='cardName',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='cardNumber',
            field=models.IntegerField(default='0', primary_key=True, serialize=False),
        ),
    ]
