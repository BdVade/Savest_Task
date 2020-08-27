from django.contrib import admin
from .models import User,UserMetrics
from django.contrib.auth.admin import UserAdmin
from datetime import datetime, timedelta



# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff',)
    list_filter = ['date_joined', 'is_staff', 'is_superuser', 'is_active', 'groups']
    list_editable = ['is_active', ]

    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)

    activate.short_description = 'activate a user'

    def disactivate(self, request, queryset):
        queryset.update(is_active=False)

    disactivate.short_description = "Make a user inactive"


@admin.register(UserMetrics)
class UserMetricAdmin(admin.ModelAdmin):
    list_display = ['result']

    def daily_new_users(self,qs):
        time_threshold = datetime.now() - timedelta(hours=24)
        result = qs.objects.filter(date_joined__lt=time_threshold).count()
        return result
