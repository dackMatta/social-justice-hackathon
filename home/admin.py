from django.contrib import admin
from . models import Case,Authority

# Register your models here.
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_type', 'description', 'status','phone_number','location')
    search_fields=('case_type','status','location')

@admin.register(Authority)
class AuthorityAdmin(admin.ModelAdmin):
    list_display=('names','department','location','charges')
    search_fields=('names','department','location')

