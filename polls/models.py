import datetime
import uuid

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


# User model definition
class User(models.Model):
    PHONE_TYPE = [
        ('M', 'Mobile'),
        ('O', 'Office')
    ]
    object = None
    user_guid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False, editable=False)
    user_name = models.CharField(max_length=254, blank=False, default='empty')
    first_name = models.CharField(max_length=254, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    phone_type = models.CharField(choices=PHONE_TYPE, max_length=1, blank=True)
    country_name = models.ForeignKey('Country', on_delete=models.CASCADE, default=840)
    street_address_1 = models.CharField(max_length=254, blank=False, default='empty')
    street_address_2 = models.CharField(max_length=254, blank=True)
    apt_suit = models.CharField(max_length=50, blank=True)
    town_name = models.ForeignKey('USTown', on_delete=models.CASCADE, default=0)
    county_name = models.ForeignKey('USCounty', on_delete=models.CASCADE, default=0)
    state_name = models.ForeignKey('USState', on_delete=models.CASCADE, default=0)
    postal_code = models.CharField(max_length=20, blank=False, default='00000')
    postal_code_9 = models.CharField(max_length=20, blank=True)
    business_category = models.ForeignKey('BusinessCategory', on_delete=models.CASCADE, default=0)
    signature_name = models.CharField(max_length=254, blank=True)
    signature_title = models.CharField(max_length=254, blank=True)
    signature_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    drivers_license_number = models.CharField(max_length=20, blank=False, default='empty')
    drivers_license_issue_date = models.DateField(default='9999-12-31')
    drivers_license_exp_date = models.DateField(default='9999-12-31')
    drivers_license_front = models.FileField(verbose_name='Picture DL front', blank=True)
    drivers_license_back = models.FileField(verbose_name='Picture DL back', blank=True)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    is_community_owner = models.BooleanField(default=False)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, blank=True)
    disabled_timestamp = models.DateTimeField(auto_now=False, blank=True)

    def __str__(self):
        return self.user_name


# User TINs model definition. Permissible to have many, but at least one is required.
class UserTINs(models.Model):
    user_tin_id = models.AutoField(primary_key=True)
    user_guid = models.ForeignKey('User', on_delete=models.CASCADE)
    tin_id = models.ForeignKey('TIN', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)
    disabled_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)

    class Meta:
        verbose_name_plural = 'User TINs'



# User Tax Identification Numbers model definition, by jurisdiction and tax type.
class TIN(models.Model):
    TIN_TYPE = [
        ('EIN', 'EIN'),
        ('TIN', 'TIN'),
        ('SSN', 'SSN'),
        ('STN', 'STID'),
    ]
    tax_code_id = models.AutoField(primary_key=True)
    tin_type = models.CharField(choices=TIN_TYPE, max_length=3)
    tin_code = models.CharField(max_length=254)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, default=840)
    state_id = models.ForeignKey('USState', on_delete=models.CASCADE, default=0)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)
    disabled_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)

    class Meta:
        verbose_name_plural = 'Tax Identifiers'


# Community model definition
class Community(models.Model):
    PHONE_TYPE = [
        ('M', 'Mobile'),
        ('O', 'Office')
    ]
    object = None
    community_guid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False, editable=False)
    community_code = models.CharField(max_length=254, blank=False, default='empty')
    community_name = models.CharField(max_length=254, blank=False, default='empty')
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    phone_type = models.CharField(choices=PHONE_TYPE, max_length=1, blank=True)
    country_name = models.ForeignKey('Country', on_delete=models.CASCADE, default=840)
    street_address_1 = models.CharField(max_length=254, blank=False, default='empty')
    street_address_2 = models.CharField(max_length=254, blank=True)
    apt_suit = models.CharField(max_length=50, blank=True)
    town_name = models.ForeignKey('USTown', on_delete=models.CASCADE, default=0)
    county_name = models.ForeignKey('USCounty', on_delete=models.CASCADE, default=0)
    state_name = models.ForeignKey('USState', on_delete=models.CASCADE, default=0)
    postal_code = models.CharField(max_length=20, blank=False, default='00000')
    postal_code_9 = models.CharField(max_length=20, blank=True)
    business_category = models.ForeignKey('BusinessCategory', on_delete=models.CASCADE, default=0)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    is_community_owner = models.BooleanField(default=False)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)
    disabled_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)

    class Meta:
        verbose_name_plural = 'Communities'

    def __str__(self):
        return self.community_name


# Community TINs model definition. Permissible to have many, but at least one is required.
class CommunityTINs(models.Model):
    community_tin_id = models.AutoField(primary_key=True)
    community_guid = models.ForeignKey('Community', on_delete=models.CASCADE)
    tin_id = models.ForeignKey('TIN', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)
    disabled_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)

    class Meta:
        verbose_name_plural = 'Community TINs'


# Community relationship hierarchy model definition.
class CommunityHierarchy(models.Model):
    RELATIONSHIP_TYPE = [
        (1, 'Parent_Child'),
        (2, 'Sibling_Sibling')
    ]
    parentCommunityGUID = models.CharField(max_length=36)
    childCommunityGUID = models.CharField(max_length=36)
    relationshipType = models.IntegerField(choices=RELATIONSHIP_TYPE, default=1, blank=True)
    can_share = models.BooleanField(default=True)
    can_view =  models.BooleanField(default=True)
    can_manage =  models.BooleanField(default=False)
    can_report =  models.BooleanField(default=True)
    can_analyze =  models.BooleanField(default=True)
    can_audit =  models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)
    deleted_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)

    class Meta:
        verbose_name_plural = 'Community Hierarchy'


# Membership model definition.
class Membership(models.Model):
    ROLE_CODE = [
        (0, 'Member'),
        (1, 'Owner'),
        (2, 'Tax Authority'),
        (3, 'XMPT')
    ]
    membership_id = models.IntegerField(primary_key=True)
    user_guid = models.ForeignKey('User', on_delete=models.CASCADE)
    community_guid = models.ForeignKey('Community', on_delete=models.CASCADE)
    roleCode = models.SmallIntegerField(choices=ROLE_CODE, default=0)  # '0 - Member, 1 - Owner, 2 - Tax Authority, 3 - XMPT'
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    deactivated_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)
    disabled_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)


# Certificate model definition
class XmptCertificate(models.Model):
    certificate_guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer_user_guid = models.CharField(max_length=36)
    seller_user_guid = models.CharField(max_length=36)
    tax_form_id = models.ForeignKey('TaxForm', on_delete=models.CASCADE)
    certificate_qr_code = models.ImageField(width_field=200, height_field=200)
    certificate_description = models.TextField()
    certificate_type = models.CharField(max_length=254, blank=True)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    expired_timestamp = models.DateTimeField(auto_now=False, default='9999-12-31 00:00', blank=True)


# Tax forms model definition.
class TaxForm(models.Model):
    tax_form_id = models.IntegerField(primary_key=True)
    tax_form_name = models.CharField(max_length=254, blank=True)
    jurisdiction_name = models.CharField(max_length=254, blank=True)

    class Meta:
        verbose_name = 'Tax Form'
        verbose_name_plural = 'Tax Forms'

    def __str__(self):
        return self.tax_form_name


# Tax Authority model definition.
class TaxAuthority(models.Model):
    tax_authority_guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    community_guid = models.ForeignKey('Community', on_delete=models.CASCADE)
    state_id = models.ForeignKey('USState', on_delete=models.CASCADE, default=0)
    state_name = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = 'Tax Authorities'


# Country model definition, uses ISO3166 standard
class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_alpha2 = models.CharField(max_length=2, blank=False)
    country_alpha3 = models.CharField(max_length=3, blank=False)
    country_name = models.CharField(max_length=254, blank=False)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name


# State model definition, uses FIPS Codes
class USState(models.Model):
    state_id = models.IntegerField(primary_key=True, default=0)
    state_alpha2 = models.CharField(max_length=2, default='ZZ')
    state_name = models.CharField(max_length=254, blank=False, default='ZZ')
    jurisdiction_level_code = models.CharField(max_length=10, blank=True)
    state_FIPS_code = models.CharField(max_length=10, blank=True)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, default=840)
    country_alpha2 = models.CharField(max_length=2, blank=False, default='US')
    country_alpha3 = models.CharField(max_length=3, blank=False, default='USA')
    country_name = models.CharField(max_length=254, blank=False,
                                   default='United States of America')

    class Meta:
        verbose_name = 'US State'
        verbose_name_plural = 'US States'

    def __str__(self):
        return self.state_name


# County model definition, uses FIPS Codes
class USCounty(models.Model):
    county_id = models.IntegerField(primary_key=True)
    state_id = models.ForeignKey('USState', on_delete=models.CASCADE, default=0)
    state_alpha2 = models.CharField(max_length=2, default='ZZ')
    state_FIPS_code = models.CharField(max_length=10, blank=True)
    county_FIPS_code = models.CharField(max_length=10, blank=True)
    county_subdivision_FIPS_code = models.CharField(max_length=10, blank=True)
    county_name = models.CharField(max_length=254, blank=False)
    jurisdiction_level_code = models.CharField(max_length=10, blank=True)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, default=840)
    country_alpha2 = models.CharField(max_length=2, blank=False, default='US')
    country_alpha3 = models.CharField(max_length=3, blank=False, default='USA')
    country_name = models.CharField(max_length=254, blank=False,
                                   default='United States of America')

    class Meta:
        verbose_name_plural = 'US Counties'

    def __str__(self):
        return self.county_name


# Town/City model definition, uses FIPS Codes
class USTown(models.Model):
    town_id = models.IntegerField(primary_key=True)
    state_FIPS_code = models.CharField(max_length=10, blank=True)
    county_FIPS_code = models.CharField(max_length=10, blank=True)
    county_subdivision_FIPS_code = models.CharField(max_length=10, blank=True)
    place_FIPS_code = models.CharField(max_length=10, blank=True)
    city_FIPS_code = models.CharField(max_length=10, blank=True)
    town_name = models.CharField(max_length=254, blank=False)
    jurisdiction_level_code = models.CharField(max_length=10, blank=True)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, default=840)
    state_id = models.ForeignKey('USState', on_delete=models.CASCADE, default=0)
    state_alpha2 = models.CharField(max_length=2, default='ZZ')
    country_alpha2 = models.CharField(max_length=2, blank=False, default='US')
    country_alpha3 = models.CharField(max_length=3, blank=False, default='USA')
    country_name = models.CharField(max_length=254, blank=False,
                                   default='United States of America')
    class Meta:
        verbose_name_plural = 'US Towns'

    def __str__(self):
        return self.town_name


# NAICS business category model definition.
class BusinessCategory(models.Model):
    business_category_id = models.AutoField(primary_key=True)
    business_category_code = models.CharField(max_length=254, blank=False)
    business_category_title = models.CharField(max_length=254, blank=False)
    version_year = models.CharField(max_length=10, default='2017')

    class Meta:
        verbose_name_plural = 'Business Categories'

    def __str__(self):
        return self.business_category_title