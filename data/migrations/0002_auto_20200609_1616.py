# Generated by Django 2.1.1 on 2020-06-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorFeatures',
            fields=[
                ('date', models.DateField(db_column='Date', primary_key=True, serialize=False)),
                ('perform_fund_situation', models.IntegerField(blank=True, db_column='Perform_Fund_Situation', null=True)),
                ('outlook_dom_demand', models.IntegerField(blank=True, db_column='Outlook_Dom_Demand', null=True)),
                ('delay_money_recovery', models.IntegerField(blank=True, db_column='Delay_Money_Recovery', null=True)),
                ('difficulty_financing', models.IntegerField(blank=True, db_column='Difficulty_Financing', null=True)),
                ('perform_oper_profit', models.IntegerField(blank=True, db_column='Perform_Oper_Profit', null=True)),
                ('competition_corporates', models.IntegerField(blank=True, db_column='Competition_Corporates', null=True)),
                ('outlook_business', models.IntegerField(blank=True, db_column='Outlook_Business', null=True)),
                ('difficulty_manpower', models.IntegerField(blank=True, db_column='Difficulty_Manpower', null=True)),
                ('rise_labor_costs', models.IntegerField(blank=True, db_column='Rise_Labor_Costs', null=True)),
                ('outlook_export', models.IntegerField(blank=True, db_column='Outlook_Export', null=True)),
            ],
            options={
                'db_table': 'cor_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Corporates',
            fields=[
                ('cor_code', models.IntegerField(db_column='Cor_code', primary_key=True, serialize=False)),
                ('region', models.CharField(blank=True, db_column='Region', max_length=10, null=True)),
            ],
            options={
                'db_table': 'corporates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorRisk',
            fields=[
                ('risk_bankruptcy', models.FloatField(blank=True, db_column='Risk_Bankruptcy', null=True)),
                ('cor_code', models.IntegerField(db_column='Cor_code', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
            ],
            options={
                'db_table': 'cor_risk',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]
