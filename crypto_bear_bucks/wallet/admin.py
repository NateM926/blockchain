from django.contrib import admin

# Register your models here.
from django_cc.cc.models import Wallet, Currency

class WalletAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wallet, WalletAdmin)