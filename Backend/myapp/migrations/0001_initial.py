# Generated by Django 4.2.6 on 2023-10-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disclosure_data_fy16',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.TextField()),
                ('case_submitted', models.DateField()),
                ('case_status', models.TextField()),
                ('decision_date', models.DateField()),
                ('visa_class', models.TextField()),
                ('employment_start_date', models.DateField()),
                ('employment_end_date', models.DateField()),
                ('employer_name', models.TextField()),
                ('employer_address', models.TextField()),
                ('employer_city', models.TextField()),
                ('employer_state', models.TextField()),
                ('employer_postal_code', models.TextField()),
                ('employer_country', models.TextField()),
                ('employer_province', models.TextField()),
                ('employer_phone', models.TextField()),
                ('agent_attorney_name', models.TextField()),
                ('agent_attorney_city', models.TextField()),
                ('agent_attorney_state', models.TextField()),
                ('job_title', models.TextField()),
                ('soc_code', models.TextField()),
                ('soc_name', models.TextField()),
                ('naic_code', models.TextField()),
                ('total_workers', models.TextField()),
                ('full_time_position', models.TextField()),
                ('prevailing_wage', models.TextField()),
                ('pw_unit_of_pay', models.TextField()),
                ('pw_wage_source', models.TextField()),
                ('pw_source_year', models.TextField()),
                ('pw_source_other', models.TextField()),
                ('wage_rate_of_pay_from', models.TextField()),
                ('wage_rate_of_pay_to', models.TextField()),
                ('wage_unit_of_pay', models.TextField()),
                ('h1bdependent', models.TextField()),
                ('willful_violator', models.TextField()),
                ('worksite_city', models.TextField()),
                ('worksite_county', models.TextField()),
                ('worksite_state', models.TextField()),
                ('worksite_postal_code', models.TextField()),
                ('original_cert_date', models.TextField()),
            ],
        ),
    ]
