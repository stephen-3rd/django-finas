from django.contrib import admin
from .models import Lust, ReachMe


class LustAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'status', 'date', 'time')
    list_filter = ('status',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}

class ReachMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')
    search_fields = ('name', 'email',)

# Register your models here.


admin.site.register(Lust, LustAdmin)
admin.site.register(ReachMe, ReachMeAdmin)