from django.contrib import admin

from xmpt.models import Choice, Question, User, UserTINs, TIN, Community, CommunityTINs, CommunityHierarchy, Membership, \
    XmptCertificate, TaxForm, TaxAuthority, Country, USState, USCounty, USTown, BusinessCategory
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register the above classes
admin.site.register(Question, QuestionAdmin)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserTINs)
class UserTINsAdmin(admin.ModelAdmin):
    pass

@admin.register(TIN)
class TINAdmin(admin.ModelAdmin):
    pass

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass

@admin.register(CommunityTINs)
class CommunityTINsAdmin(admin.ModelAdmin):
    pass

@admin.register(CommunityHierarchy)
class CommunityHierarchyAdmin(admin.ModelAdmin):
    pass

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass

@admin.register(XmptCertificate)
class XMPTCertificateAdmin(admin.ModelAdmin):
    pass

@admin.register(TaxForm)
class TaxFormAdmin(admin.ModelAdmin):
    pass

@admin.register(TaxAuthority)
class TaxAuthorityAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ['country_name', 'country_alpha2', 'country_alpha3', 'country_id']
    list_display = ['country_name', 'country_alpha2', 'country_alpha3','country_id']
    list_filter = ['country_name']
    search_fields = ['country_name']
    list_per_page = 50

@admin.register(USState)
class USStateAdmin(admin.ModelAdmin):
    fields = ['state_name', 'state_alpha2', 'state_id', 'state_fips_code']
    list_display = ['state_name', 'state_alpha2', 'state_id', 'state_fips_code']
    ordering = ['state_alpha2']
    search_fields = ['state_name']

@admin.register(USCounty)
class USCountyAdmin(admin.ModelAdmin):
    fields = ['county_name', 'county_id', 'state_alpha2', 'county_fips_code', 'county_subdivision_fips_code']
    list_display = ['county_name', 'county_id', 'state_alpha2', 'county_fips_code', 'county_subdivision_fips_code']
    list_filter = ['state_id']
    ordering = ['state_alpha2', 'county_name']
    search_fields = ['state_name', 'county_name']
    list_per_page = 50
    list_select_related = True

@admin.register(USTown)
class USTownAdmin(admin.ModelAdmin):
    fields = ['town_name', 'city_fips_code', 'town_id', 'state_alpha2', 'county']
    list_display = ['town_name', 'town_id', 'state_alpha2', 'county_fips_code', 'county_subdivision_fips_code']
    list_filter = ['state_id']
    ordering = ['town_name']
    search_fields = ['town_name', 'state_name']
    list_per_page = 50
    list_select_related = True

@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    fields = ['business_category_id', 'business_category_code', 'business_category_title', 'version_year']
    list_display = ['business_category_title', 'business_category_code']
    list_select_related = True
    ordering = ['business_category_title']
    # list_filter = ['business_category_title']
    search_fields = ['business_category_title', 'business_category_code']
    list_per_page = 50

