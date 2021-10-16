from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



# General Admin.

admin.site.site_title = 'book App Admin'
admin.site.site_header ='book App Administration'
admin.site.index_title ='book APP Site Admin'



# images associated with the book

class imgadmin(admin.TabularInline):
    model = img_addon
    extra = 0
    max_num = 100

# chapter associated with the book

class chapteradmin(admin.TabularInline):
    model = chapter
    extra = 0
    max_num = 100

# faq associated with the book

@admin.register(book_list)
class ViewAdmin(ImportExportModelAdmin):
    inlines = [imgadmin,chapteradmin]
    list_display = (
            'book_title',
            'book_code',
            'book_description',
        )
    class Meta:
       model = book_list 

@admin.register(img_addon)
class imgadmin(admin.ModelAdmin):
    pass

@admin.register(chapter)
class imgadmin(admin.ModelAdmin):
    pass

@admin.register(services)
class ViewAdmin(ImportExportModelAdmin):
    list_display = (
            'service_title',
            'service_fee',
        )
    class Meta:
       model = services


@admin.register(servicesubscription)
class ViewAdmin(ImportExportModelAdmin):
    list_display = (
            'sub_id',
            'txn_date',
            'exp_date',
            'txn_id',
            'service_id',
            'creation_date',
        )
    class Meta:
       model = servicesubscription
