# Generated by Django 3.1.7 on 2021-03-24 17:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('xmpt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('business_category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('business_category_code', models.CharField(max_length=254)),
                ('business_category_title', models.CharField(max_length=254)),
                ('version_year', models.CharField(default='2017', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Business Categories',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('community_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('community_code', models.CharField(default='empty', max_length=254)),
                ('community_name', models.CharField(default='empty', max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('phone_type', models.CharField(blank=True, choices=[('M', 'Mobile'), ('O', 'Office')], max_length=1)),
                ('street_address_1', models.CharField(default='empty', max_length=254)),
                ('street_address_2', models.CharField(blank=True, max_length=254)),
                ('apt_suit', models.CharField(blank=True, max_length=50)),
                ('postal_code', models.CharField(default='00000', max_length=20)),
                ('postal_code_9', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('is_community_owner', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('disabled_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('business_category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.businesscategory')),
            ],
            options={
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='CommunityHierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentCommunityGUID', models.CharField(max_length=36)),
                ('childCommunityGUID', models.CharField(max_length=36)),
                ('relationshipType', models.IntegerField(blank=True, choices=[(1, 'Parent_Child'), (2, 'Sibling_Sibling')], default=1)),
                ('can_share', models.BooleanField(default=True)),
                ('can_view', models.BooleanField(default=True)),
                ('can_manage', models.BooleanField(default=False)),
                ('can_report', models.BooleanField(default=True)),
                ('can_analyze', models.BooleanField(default=True)),
                ('can_audit', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('deleted_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
            ],
            options={
                'verbose_name_plural': 'Community Hierarchy',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_alpha2', models.CharField(max_length=2)),
                ('country_alpha3', models.CharField(max_length=3)),
                ('country_name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='TaxForm',
            fields=[
                ('tax_form_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tax_form_name', models.CharField(blank=True, max_length=254)),
                ('jurisdiction_name', models.CharField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'Tax Form',
                'verbose_name_plural': 'Tax Forms',
            },
        ),
        migrations.CreateModel(
            name='TIN',
            fields=[
                ('tax_code_id', models.AutoField(primary_key=True, serialize=False)),
                ('tin_type', models.CharField(choices=[('EIN', 'EIN'), ('TIN', 'TIN'), ('SSN', 'SSN'), ('STN', 'STID')], max_length=3)),
                ('tin_code', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('disabled_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('country_id', models.ForeignKey(default=840, on_delete=django.db.models.deletion.CASCADE, to='xmpt.country')),
            ],
            options={
                'verbose_name_plural': 'Tax Identifiers',
            },
        ),
        migrations.CreateModel(
            name='USCounty',
            fields=[
                ('county_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_alpha2', models.CharField(default='ZZ', max_length=2)),
                ('state_fips_code', models.CharField(blank=True, max_length=10)),
                ('county_fips_code', models.CharField(blank=True, max_length=10)),
                ('county_subdivision_fips_code', models.CharField(blank=True, max_length=10)),
                ('county_name', models.CharField(max_length=254)),
                ('jurisdiction_level_code', models.CharField(blank=True, max_length=10)),
                ('country_alpha2', models.CharField(default='US', max_length=2)),
                ('country_alpha3', models.CharField(default='USA', max_length=3)),
                ('country_name', models.CharField(default='United States of America', max_length=254)),
                ('country_id', models.ForeignKey(default=840, on_delete=django.db.models.deletion.CASCADE, to='xmpt.country')),
            ],
            options={
                'verbose_name_plural': 'US Counties',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='empty', max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('phone_type', models.CharField(blank=True, choices=[('M', 'Mobile'), ('O', 'Office')], max_length=1)),
                ('street_address_1', models.CharField(default='empty', max_length=254)),
                ('street_address_2', models.CharField(blank=True, max_length=254)),
                ('apt_suit', models.CharField(blank=True, max_length=50)),
                ('postal_code', models.CharField(default='00000', max_length=20)),
                ('postal_code_9', models.CharField(blank=True, max_length=20)),
                ('signature_name', models.CharField(blank=True, max_length=254)),
                ('signature_title', models.CharField(blank=True, max_length=254)),
                ('signature_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('drivers_license_number', models.CharField(default='empty', max_length=20)),
                ('drivers_license_issue_date', models.DateField(default='9999-12-31')),
                ('drivers_license_exp_date', models.DateField(default='9999-12-31')),
                ('drivers_license_front', models.FileField(blank=True, upload_to='', verbose_name='Picture DL front')),
                ('drivers_license_back', models.FileField(blank=True, upload_to='', verbose_name='Picture DL back')),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('is_community_owner', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True)),
                ('disabled_timestamp', models.DateTimeField(blank=True)),
                ('business_category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.businesscategory')),
                ('country_name', models.ForeignKey(default=840, on_delete=django.db.models.deletion.CASCADE, to='xmpt.country')),
                ('county_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.uscounty')),
            ],
        ),
        migrations.CreateModel(
            name='USState',
            fields=[
                ('state_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('state_alpha2', models.CharField(default='ZZ', max_length=2)),
                ('state_name', models.CharField(default='ZZ', max_length=254)),
                ('jurisdiction_level_code', models.CharField(blank=True, max_length=10)),
                ('state_fips_code', models.CharField(blank=True, max_length=10)),
                ('country_alpha2', models.CharField(default='US', max_length=2)),
                ('country_alpha3', models.CharField(default='USA', max_length=3)),
                ('country_name', models.CharField(default='United States of America', max_length=254)),
                ('country_id', models.ForeignKey(default=840, on_delete=django.db.models.deletion.CASCADE, to='xmpt.country')),
            ],
            options={
                'verbose_name': 'US State',
                'verbose_name_plural': 'US States',
            },
        ),
        migrations.CreateModel(
            name='XmptCertificate',
            fields=[
                ('certificate_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('buyer_user_guid', models.CharField(max_length=36)),
                ('seller_user_guid', models.CharField(max_length=36)),
                ('certificate_qr_code', models.ImageField(height_field=200, upload_to='', width_field=200)),
                ('certificate_description', models.TextField()),
                ('certificate_type', models.CharField(blank=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('expired_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('tax_form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.taxform')),
            ],
        ),
        migrations.CreateModel(
            name='USTown',
            fields=[
                ('town_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_fips_code', models.CharField(blank=True, max_length=10)),
                ('county_fips_code', models.CharField(blank=True, max_length=10)),
                ('county_subdivision_fips_code', models.CharField(blank=True, max_length=10)),
                ('place_fips_code', models.CharField(blank=True, max_length=10)),
                ('city_fips_code', models.CharField(blank=True, max_length=10)),
                ('town_name', models.CharField(max_length=254)),
                ('jurisdiction_level_code', models.CharField(blank=True, max_length=10)),
                ('state_alpha2', models.CharField(default='ZZ', max_length=2)),
                ('country_alpha2', models.CharField(default='US', max_length=2)),
                ('country_alpha3', models.CharField(default='USA', max_length=3)),
                ('country_name', models.CharField(default='United States of America', max_length=254)),
                ('country_id', models.ForeignKey(default=840, on_delete=django.db.models.deletion.CASCADE, to='xmpt.country')),
                ('state_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.usstate')),
            ],
            options={
                'verbose_name_plural': 'US Towns',
            },
        ),
        migrations.CreateModel(
            name='UserTINs',
            fields=[
                ('user_tin_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('disabled_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('tin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.tin')),
                ('user_guid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.user')),
            ],
            options={
                'verbose_name_plural': 'User TINs',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='state_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.usstate'),
        ),
        migrations.AddField(
            model_name='user',
            name='town_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.ustown'),
        ),
        migrations.AddField(
            model_name='uscounty',
            name='state_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.usstate'),
        ),
        migrations.AddField(
            model_name='tin',
            name='state_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.usstate'),
        ),
        migrations.CreateModel(
            name='TaxAuthority',
            fields=[
                ('tax_authority_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('community_guid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.community')),
                ('state_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.usstate')),
            ],
            options={
                'verbose_name_plural': 'Tax Authorities',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.IntegerField(primary_key=True, serialize=False)),
                ('roleCode', models.SmallIntegerField(choices=[(0, 'Member'), (1, 'Owner'), (2, 'Tax Authority'), (3, 'XMPT')], default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('disabled_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('community_guid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.community')),
                ('user_guid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.user')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityTINs',
            fields=[
                ('community_tin_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('deactivated_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('disabled_timestamp', models.DateTimeField(blank=True, default='9999-12-31 00:00')),
                ('community_guid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.community')),
                ('tin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmpt.tin')),
            ],
            options={
                'verbose_name_plural': 'Community TINs',
            },
        ),
        migrations.AddField(
            model_name='community',
            name='country_name',
            field=models.ForeignKey(default=840, on_delete=django.db.models.deletion.CASCADE, to='xmpt.country'),
        ),
        migrations.AddField(
            model_name='community',
            name='county_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.uscounty'),
        ),
        migrations.AddField(
            model_name='community',
            name='state_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.usstate'),
        ),
        migrations.AddField(
            model_name='community',
            name='town_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='xmpt.ustown'),
        ),
    ]
