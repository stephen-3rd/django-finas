from django.contrib import admin
from .models import Lust


class LustAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'status', 'date', 'time')
    list_filter = ('status',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.


admin.site.register(Lust, LustAdmin)
