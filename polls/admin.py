from django.contrib import admin

from polls.models import Choice, Question, User, UserTINs, TIN, Community, CommunityTINs, CommunityHierarchy, Membership, \
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
    pass

@admin.register(USState)
class USStateAdmin(admin.ModelAdmin):
    pass

@admin.register(USCounty)
class USCountyAdmin(admin.ModelAdmin):
    pass

@admin.register(USTown)
class USTownAdmin(admin.ModelAdmin):
    pass

@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    pass

