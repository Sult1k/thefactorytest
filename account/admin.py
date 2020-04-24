from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'chat_id', 'token', 'last_login', 'date_joined')
    search_fields = ('id', 'username', 'first_name',)
    readonly_fields = ('date_joined', 'last_login', 'id')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
# Register your models here.
