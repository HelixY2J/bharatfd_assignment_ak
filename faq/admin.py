from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):

    list_display = ['id', 'question']
    search_fields = ['id', 'question']
    list_filter = ['id']
    list_per_page = 20

admin.site.site_header = 'FAQs Admin'
admin.site.site_title = 'FAQs Management Admin HQ'
admin.site.index_title = 'Welcome- FAQs Admin Area :>'
admin.site.register(FAQ, FAQAdmin)