from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):

    list_display = ['id', 'question', 'que_hindi', 'que_bengali']
    search_fields = ['id', 'question', 'que_hindi', 'que_bengali']
    list_filter = ['que_hindi', 'que_bengali']
    ordering = ['question']


admin.site.site_header = 'FAQs Admin'
admin.site.site_title = 'FAQs Management Admin HQ'
admin.site.index_title = 'Welcome- FAQs Admin Area :>'
admin.site.register(FAQ, FAQAdmin)