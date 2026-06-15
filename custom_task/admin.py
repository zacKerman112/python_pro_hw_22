from django.contrib import admin
from .models import UserConfig, UserLog


class UserLogInline(admin.TabularInline):
    model = UserLog
    extra = 1


@admin.register(UserConfig)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'bio')
    list_filter = ('username',)
    inlines = [UserLogInline]
    actions = ['clear_bio']
    
    @admin.action(description='Clean bio for certain user')
    def clear_bio(self, request, queryset):
        """cleared bio alhorythm"""
        queryset.update(bio='')
    fieldsets = (
        ('Main Information', {
            'fields': ('username', 'bio')
        }),
        ('Additional information', {
            'fields': ('settings',),
        }),
    )